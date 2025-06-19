import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

# 3-letter codes untuk kota
city_codes = {
    "Jakarta": "JKT",
    "Bandung": "BDG",
    "Semarang": "SMG",
    "Yogyakarta": "YGY",
    "Surabaya": "SBY",
    "Medan": "MDN",
    "Padang": "PDG",
    "Palembang": "PLB",
    "Pekanbaru": "PKU",
    "Jambi": "JBI"
}

# Latitude dan Longitude kota
cities = {
    "Jakarta": (-6.175110, 106.865036),
    "Bandung": (-6.917464, 107.619125),
    "Semarang": (-7.005145, 110.438126),
    "Yogyakarta": (-7.795580, 110.369492),
    "Surabaya": (-7.257472, 112.752090),
    "Medan": (3.595196, 98.672226),
    "Padang": (-0.947083, 100.417183),
    "Palembang": (-2.976074, 104.775429),
    "Pekanbaru": (0.507068, 101.447777),
    "Jambi": (-1.610123, 103.613121)
}

# Fungsi haversine untuk menghitung jarak antar koordinat
def haversine(coord1, coord2):
    R = 6371  # radius bumi dalam km
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Threshold koneksi antar kota (dalam km)
threshold_km = 1000
city_names = list(cities.keys())
n = len(city_names)
adj_matrix = np.zeros((n, n))
adj_list = {city_codes[city]: [] for city in city_names}

for i in range(n):
    for j in range(n):
        if i != j:
            dist = haversine(cities[city_names[i]], cities[city_names[j]])
            if dist <= threshold_km:
                rounded_dist = round(dist)
                code_i = city_codes[city_names[i]]
                code_j = city_codes[city_names[j]]
                adj_matrix[i][j] = rounded_dist
                adj_list[code_i].append((code_j, rounded_dist))

code_labels = [city_codes[name] for name in city_names]
adj_df = pd.DataFrame(adj_matrix, index=code_labels, columns=code_labels)
adj_df.to_csv("adj_matrix.csv")

adj_list_df = pd.DataFrame([
    {"From": src, "To": dst, "Distance": dist}
    for src, neighbors in adj_list.items()
    for dst, dist in neighbors
])
adj_list_df.to_csv("adj_list.csv", index=False)
