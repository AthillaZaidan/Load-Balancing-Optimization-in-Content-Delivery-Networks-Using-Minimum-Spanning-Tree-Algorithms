class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def lam_mst(edges, nodes, alpha=1):
    deg = {node: 0 for node in nodes}
    mst = []
    total_cost = 0
    uf = UnionFind(nodes)

    while len(mst) < len(nodes) - 1:
        modified_edges = sorted(
            edges, key=lambda x: x[2] + alpha * (deg[x[0]] + deg[x[1]])
        )

        for u, v, w in modified_edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                deg[u] += 1
                deg[v] += 1
                mst.append((u, v, w))
                total_cost += w
                break

    return mst, total_cost