from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary: old node → new node
        visited = {}

        # Create clone of the starting node
        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # Create clone of neighbor
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Link the clone of neighbor to clone of current node
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]