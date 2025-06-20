
# 📦 Load-Balancing Optimization in Content Delivery Networks Using Minimum Spanning Tree Algorithms

This project implements and compares two algorithms for optimizing content delivery network (CDN) topologies:

- 🔹 **Kruskal's Minimum Spanning Tree (MST)** — standard cost-minimization
- 🔸 **Load-Aware Modified MST (LAM-MST)** — balances traffic load using node degree penalties

Implemented in **Python**, this simulation is tested on a synthetic graph of 10 major cities in Indonesia, connected based on geographical proximity (≤ 1000 km).

---

## 📁 Project Structure

```
.
├── src/
│   ├── GraphGenerator.py         # Generate adjacency list from city coordinates
│   ├── Kruskal_Algorithm.py      # Classic Kruskal's MST implementation
│   ├── LAM_MST_Algorithm.py      # Load-Aware Modified MST
│   ├── main.py                   # Main evaluation script
│   └── 50cities_experimental/    # Experiment with 50 cities (Dataset + results) (optional)
├── docs/                         # docs for this experiment
├── README.md                     # You're reading it
```

---

## 🛠 Requirements

Make sure you have Python ≥ 3.8 and the following libraries:

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd src
python main.py
```

Expected output includes:

- The edge list of both MST and LAM-MST
- Total cost
- Maximum node degree
- Standard deviation of degree
- Degree distribution across all nodes

---

## 📐 Algorithmic Summary

- **Kruskal's MST** minimizes the total connection cost but may result in centralized, unbalanced load on certain nodes.
- **LAM-MST** modifies the edge weight using:

  `W'(u,v) = w(u,v) + α · (deg(u) + deg(v))`


  A higher α penalizes edges connected to high-degree nodes, thus encouraging load balancing.

---

## 📊 Dataset

The dataset used is a synthetic 10-city graph based on real geographical coordinates. Edge weights represent great-circle distances using the Haversine formula. Also, there is an experiment using 50 cities that can be accessed in the src/50cities_experimental/

---

## 📚 References

- Rinaldi Munir – [IF1220 Discrete Mathematics Lecture Notes](https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/)
- Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, 7th ed., 2012.
- Pathan & Al-Shaer, *An Introduction to Content Delivery Networks*, 2008.
- Al-Fuqaha et al., *A Novel Load Balancing Mechanism for RPL*, WiMob 2016.

---

## ✍️ Author

Athilla Zaidan Zidna Fann – 13524068  
Informatics Engineering – STEI ITB
