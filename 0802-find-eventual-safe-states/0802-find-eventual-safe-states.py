class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0 = unvisited, 1 = visiting, 2 = safe
        color = [0] * n

        def dfs(node: int) -> bool:
            if color[node] == 1:      # cycle detected
                return False
            if color[node] == 2:      # already known safe
                return True

            color[node] = 1           # mark as visiting

            for nei in graph[node]:
                if not dfs(nei):      # any unsafe neighbour → unsafe
                    return False

            color[node] = 2           # all paths safe
            return True

        return [i for i in range(n) if dfs(i)]