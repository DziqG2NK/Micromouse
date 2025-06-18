
class PathFinder:
    def __init__(self, vehicle, start_node):
        self.vehicle = vehicle
        self.start = start_node

    def find_path_to_finish(self):
        def dfs(node, visited, path):
            if node is None or node in visited:
                return False
            visited.add(node)
            path.append(node)

            if node.is_finish:
                return True

            for child in [c for c in [node.up_child, node.down_child, node.left_child, node.right_child] if c is not None]:
                if dfs(child, visited, path):
                    return True

            path.pop()  # backtrack
            return False

        visited = set()
        path = []
        if dfs(self.start, visited, path):
            return path  # List of nodes from start to finish
        else:
            return None  # No path found
