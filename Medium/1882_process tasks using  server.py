import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = []
        busy = []

        # Initially, all servers are available
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                # Release all servers finishing at this time
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select server with minimum weight, then minimum index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return ans
