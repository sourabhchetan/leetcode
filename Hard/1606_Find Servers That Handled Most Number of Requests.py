import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        n = len(arrival)

        # Fenwick Tree: initially all servers are available
        bit = [0] * (k + 1)

        for i in range(1, k + 1):
            bit[i] = i & -i

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        # Number of available servers among indices [0, i-1]
        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        # Find the server having the given available rank
        def find_kth(rank):
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= k and bit[nxt] < rank:
                    idx = nxt
                    rank -= bit[nxt]

                step >>= 1

            return idx

        # (finish time, server index)
        busy = []

        handled = [0] * k

        for i in range(n):
            current_time = arrival[i]

            # Release servers that have finished
            while busy and busy[0][0] <= current_time:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Check whether any server is available
            available = query(k)

            if available == 0:
                continue

            start = i % k

            # Find first available server >= start
            before = query(start)
            rank = before + 1

            # Wrap around if necessary
            if rank > available:
                rank = 1

            server = find_kth(rank)

            # Assign the task
            update(server, -1)
            handled[server] += 1

            finish_time = current_time + load[i]
            heapq.heappush(busy, (finish_time, server))

        # Return all servers with maximum handled requests
        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]
