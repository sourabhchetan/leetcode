import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')

        # dist[node][count] = minimum cost to reach
        # node with count consecutive identical labels
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Starting node has a consecutive count of 1
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            # First popped destination state has minimum cost
            if u == n - 1:
                return cost

            for v, w in graph[u]:

                # Calculate the next consecutive count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Reject invalid paths
                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, v, new_count)
                    )

        return -1
