def biggest_descendent(graph, root, value):
    result = {}

    def dfs(node):
        biggest = value[node]

        for neighbor in graph.neighbors(node):
            biggest = max(biggest, dfs(neighbor))

        result[node] = biggest
        return biggest

    dfs(root)
    return result
