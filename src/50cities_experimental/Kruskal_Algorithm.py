class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal_mst(edges, nodes):
    # Sort edges by weight only (alpha = 0)
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(nodes)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_cost += w
            if len(mst) == len(nodes) - 1:
                break

    return mst, total_cost