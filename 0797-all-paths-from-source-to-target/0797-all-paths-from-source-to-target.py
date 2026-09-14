class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if len(graph) == 0 : return [[]]
        res = []
        def dfs(graph):
            stk = [(0,[0])]
            while stk :
                node,path = stk.pop()
                for n in range(len(graph[node])):
                    next_node = graph[node][n]
                    new_path = path + [next_node]
                    if graph[node][n] == len(graph) - 1 :
                        res.append(new_path)
                    else : stk.append((next_node,new_path))
        
        dfs(graph)
        return res
        