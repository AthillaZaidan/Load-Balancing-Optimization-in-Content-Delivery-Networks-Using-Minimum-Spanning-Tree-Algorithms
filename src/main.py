import pandas as pd
import numpy as np
from collections import defaultdict
from Kruskal_Algorithm import kruskal_mst
from LAM_MST_Algorithm import lam_mst

def evaluate_tree(mst_edges, nodes):
    degree = defaultdict(int)
    total_cost = 0

    for u, v, w in mst_edges:
        degree[u] += 1
        degree[v] += 1
        total_cost += w

    degrees = [degree[node] for node in nodes]
    max_degree = max(degrees)
    std_dev = np.std(degrees)

    return {
        "Total Cost": total_cost,
        "Max Degree": max_degree,
        "Degree Std Dev": std_dev,
        "Degree Per Node": dict(degree)
    }

def main():
    df = pd.read_csv("adj_list.csv")
    edges = list(df.itertuples(index=False, name=None))
    nodes = sorted(set(df["From"]).union(df["To"]))

    mst_kruskal, _ = kruskal_mst(edges.copy(), nodes)
    eval_kruskal = evaluate_tree(mst_kruskal, nodes)

    print("=== Kruskal's MST (α = 0) ===")
    for u, v, w in mst_kruskal:
        print(f"{u} - {v} : {w} km")
    print("\nMetrics:")
    print("Total Cost:", eval_kruskal["Total Cost"], "km")
    print("Max Degree:", eval_kruskal["Max Degree"])
    print("Degree Std Dev:", round(eval_kruskal["Degree Std Dev"], 2))
    print("Degree per Node:", eval_kruskal["Degree Per Node"])

    mst_lam, _ = lam_mst(edges.copy(), nodes, alpha=100)
    eval_lam = evaluate_tree(mst_lam, nodes)

    print("\n=== LAM-MST (α = 100) ===")
    for u, v, w in mst_lam:
        print(f"{u} - {v} : {w} km")
    print("\nMetrics:")
    print("Total Cost:", eval_lam["Total Cost"], "km")
    print("Max Degree:", eval_lam["Max Degree"])
    print("Degree Std Dev:", round(eval_lam["Degree Std Dev"], 2))
    print("Degree per Node:", eval_lam["Degree Per Node"])

if __name__ == "__main__":
    main()
