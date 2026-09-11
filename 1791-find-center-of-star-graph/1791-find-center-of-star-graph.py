class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if not edges : return None
        def build_graph(edges):
            graph = {}

            for u , v in edges:
                if u not in graph :
                    graph[u] = []

                if v not in graph:
                    graph[v] = []
                graph[u].append(v)
                graph[v].append(u)

            return graph
        graph = build_graph(edges)
        
        for key in graph :
            if len(graph[key]) == len(graph) - 1 : return key

