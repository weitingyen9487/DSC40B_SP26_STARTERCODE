from collections import deque

def assign_good_and_evil(graph):
    labels = {}

    for node in graph.nodes:

        if node in labels:
            continue

        # Start this component as "good"
        labels[node] = "good"

        queue = deque([node])

        while queue:
            current = queue.popleft()

            if labels[current] == "good":
                opposite = "evil"
            else:
                opposite = "good"

            for neighbor in graph.neighbors(current):

                if neighbor not in labels:
                    labels[neighbor] = opposite
                    queue.append(neighbor)

                # Conflict found
                elif labels[neighbor] == labels[current]:
                    return None

    return labels
