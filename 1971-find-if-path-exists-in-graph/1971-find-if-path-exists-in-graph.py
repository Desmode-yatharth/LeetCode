class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        if len(edges) == 0 : return True
        
        def build_graph(edges):
            graph = defaultdict(list)

            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)

            return graph

        graph = build_graph(edges)
        
        def dfs(graph,node,destin):
            stk = [node]
            visit = set()

            while stk :

                node = stk.pop()
                if node in visit : continue
                
                if node == destin : return True
                
                visit.add(node)

                for n in graph[node]:
                    if n not in visit : stk.append(n)

            return False

        a = dfs(graph,source,destination)

        return a

        