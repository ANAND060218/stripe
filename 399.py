
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                    queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        ans = []

        for src, dst in queries:

            # if either variable not present
            if src not in graph or dst not in graph:
                ans.append(-1.0)
                continue

            # BFS
            q = deque([(src, 1.0)])
            visited = set([src])
            found = False

            while q:
                node, value = q.popleft()

                if node == dst:
                    ans.append(value)
                    found = True
                    break

                for nei, weight in graph[node].items():
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, value * weight))

            if not found:
                ans.append(-1.0)

        return ans
