def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for node in graph.nodes():
        if node not in visited:
            component = set()
            stack = [node]
            visited.add(node)

            while stack:
                current = stack.pop()
                component.add(current)

                for neighbor in graph.neighbors(current):
                    if neighbor not in visited and weights(current, neighbor) >= level:
                        visited.add(neighbor)
                        stack.append(neighbor)

            clusters.append(frozenset(component))

    return frozenset(clusters)
