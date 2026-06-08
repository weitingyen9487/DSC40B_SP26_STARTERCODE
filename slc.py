class DisjointSetForest:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


def _get_nodes(graph):
    if hasattr(graph, "nodes"):
        nodes = graph.nodes
        return list(nodes() if callable(nodes) else nodes)
    if hasattr(graph, "vertices"):
        vertices = graph.vertices
        return list(vertices() if callable(vertices) else vertices)

    nodes = set()
    for u, v in _get_edges(graph):
        nodes.add(u)
        nodes.add(v)
    return list(nodes)


def _get_edges(graph):
    if hasattr(graph, "edges"):
        edges = graph.edges
        return list(edges() if callable(edges) else edges)

    result = []
    for u in _get_nodes(graph):
        for v in graph.neighbors(u):
            if str(u) < str(v):
                result.append((u, v))
    return result


def slc(graph, d, k):
    nodes = _get_nodes(graph)
    edges = _get_edges(graph)

    dsf = DisjointSetForest()
    for node in nodes:
        dsf.make_set(node)

    num_clusters = len(nodes)

    for u, v in sorted(edges, key=d):
        if num_clusters == k:
            break

        if dsf.union(u, v):
            num_clusters -= 1

    clusters = {}
    for node in nodes:
        root = dsf.find(node)
        if root not in clusters:
            clusters[root] = set()
        clusters[root].add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())
