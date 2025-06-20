import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

# 3-letter codes untuk kota
city_codes = {
    "Jakarta": "JKT", "Bandung": "BDG", "Surabaya": "SBY", "Medan": "MDN", "Makassar": "MKS",
    "Manado": "MDO", "Jayapura": "JYP", "Pontianak": "PTK", "Samarinda": "SMD", "Ambon": "AMB",
    "Kupang": "KPG", "Palembang": "PLB", "Padang": "PDG", "Banjarmasin": "BJM", "Balikpapan": "BPN",
    "Denpasar": "DPS", "Mataram": "MTR", "Ternate": "TRN", "Palu": "PLU", "Gorontalo": "GTO",
    "Yogyakarta": "YGY", "Semarang": "SMG", "Pekanbaru": "PKU", "Jambi": "JBI", "Kendari": "KDI",
    "Manokwari": "MNK", "Sorong": "SRG", "Tarakan": "TRK", "Bitung": "BTG", "Lhokseumawe": "LHS",
    "Aceh": "ACE", "Serang": "SRG", "Cirebon": "CRB", "Magelang": "MGL", "Bengkulu": "BKL",
    "Tual": "TUL", "Waingapu": "WGP", "Tanjungpinang": "TJP", "Singkawang": "SKW", "Bau-Bau": "BAU",
    "Pangkalpinang": "PGK", "Gunungsitoli": "GNS", "Sabang": "SBG", "Ende": "END",
    "Tebing Tinggi": "TBT", "Palopo": "PLO", "Pamekasan": "PMK", "Labuan Bajo": "LBJ", "Sibolga": "SBL"
}

cities = {
    "Jakarta": (-6.2088, 106.8456), "Bandung": (-6.9175, 107.6191), "Surabaya": (-7.2575, 112.7521),
    "Medan": (3.5952, 98.6722), "Makassar": (-5.1477, 119.4327), "Manado": (1.4748, 124.8421),
    "Jayapura": (-2.5337, 140.7181), "Pontianak": (0.0263, 109.3425), "Samarinda": (-0.5022, 117.1537),
    "Ambon": (-3.6547, 128.1906), "Kupang": (-10.1772, 123.6070), "Palembang": (-2.9909, 104.7566),
    "Padang": (-0.9471, 100.4172), "Banjarmasin": (-3.3194, 114.5908), "Balikpapan": (-1.2654, 116.8312),
    "Denpasar": (-8.6500, 115.2167), "Mataram": (-8.5833, 116.1167), "Ternate": (0.7906, 127.3900),
    "Palu": (-0.8917, 119.8707), "Gorontalo": (0.5411, 123.0595), "Yogyakarta": (-7.7956, 110.3695),
    "Semarang": (-6.9667, 110.4167), "Pekanbaru": (0.5071, 101.4478), "Jambi": (-1.6101, 103.6131),
    "Kendari": (-3.9726, 122.5120), "Manokwari": (-0.8615, 134.0781), "Sorong": (-0.8816, 131.2500),
    "Tarakan": (3.3274, 117.5785), "Bitung": (1.4433, 125.1900), "Lhokseumawe": (5.1880, 97.1416),
    "Aceh": (5.5483, 95.3238), "Serang": (-6.1214, 106.1502), "Cirebon": (-6.7063, 108.5574),
    "Magelang": (-7.4706, 110.2177), "Bengkulu": (-3.8004, 102.2655), "Tual": (-5.6336, 132.7442),
    "Waingapu": (-9.6606, 120.2641), "Tanjungpinang": (0.9167, 104.4500), "Singkawang": (0.9084, 108.9847),
    "Bau-Bau": (-5.4697, 122.6169), "Pangkalpinang": (-2.1291, 106.1133), "Gunungsitoli": (1.2906, 97.6141),
    "Sabang": (5.8897, 95.3167), "Ende": (-8.8432, 121.6625), "Tebing Tinggi": (3.3300, 99.1600),
    "Palopo": (-2.9945, 120.1960), "Pamekasan": (-7.1566, 113.4741), "Labuan Bajo": (-8.4962, 119.8877),
    "Sibolga": (1.7407, 98.7791)
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

# Bangun adjacency matrix dan list
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

# Simpan adjacency matrix ke CSV
code_labels = [city_codes[name] for name in city_names]
adj_df = pd.DataFrame(adj_matrix, index=code_labels, columns=code_labels)
adj_df.to_csv("adj_matrix_50.csv")

# Simpan adjacency list ke CSV
adj_list_df = pd.DataFrame([
    {"From": src, "To": dst, "Distance": dist}
    for src, neighbors in adj_list.items()
    for dst, dist in neighbors
])
adj_list_df.to_csv("adj_list_50.csv", index=False)
