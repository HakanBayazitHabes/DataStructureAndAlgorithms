# connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# connections = [[1,0],[1,2],[3,2],[3,4]]
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        edges = set()

        for a, b in connections:
            edges.add((a, b))

        neighbours = {}  # Dictionary

        for city in range(n):
            neighbours[city] = []

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()
        counter = 0

        def dfs(city):
            nonlocal edges, neighbours, visited, counter

            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (neighbour, city) not in edges:
                    counter += 1
                visited.add(neighbour)
                dfs(neighbour)

        visited.add(0)
        dfs(0)
        return counter


solution = Solution()
print(solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
