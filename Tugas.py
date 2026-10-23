# =========================================================
# ANALISIS DATASET BRAND FASHION LOKAL
# Analisis jenis data, duplikat, data kosong, nilai nol,
# statistik deskriptif, dan visualisasi.
# Library: numpy, pandas, scikit-learn, matplotlib
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Pastikan file CSV berada di folder yang sama dengan file Python ini.
PATH_CSV = "dataset_brand_fashion_lokal.csv"

# 1. MEMBACA DATASET
df = pd.read_csv(PATH_CSV)

print("=" * 65)
print("ANALISIS DATASET BRAND FASHION LOKAL")
print("=" * 65)
print("\n=== 5 DATA PERTAMA ===")
print(df.head())

print("\nUkuran dataset:")
print(f"Jumlah baris  : {df.shape[0]}")
print(f"Jumlah kolom  : {df.shape[1]}")

print("\n=== INFORMASI DATASET ===")
df.info()

print("\n=== STATISTIK DESKRIPTIF ===")
print(df.describe(include="all").T)

# 2. MEMISAHKAN KOLOM NUMERIK DAN KATEGORIKAL
kolom_numerik = df.select_dtypes(include=[np.number]).columns.tolist()
kolom_kategorikal = df.select_dtypes(exclude=[np.number]).columns.tolist()

jumlah_kolom = len(df.columns)
jumlah_numerik = len(kolom_numerik)
jumlah_kategorikal = len(kolom_kategorikal)

print("\n=== JENIS DATA ===")
print(f"Kolom numerik ({jumlah_numerik}): {kolom_numerik}")
print(f"Kolom kategorikal ({jumlah_kategorikal}): {kolom_kategorikal}")

print("\n=== PERSENTASE JENIS KOLOM ===")
print(f"Numerik      : {jumlah_numerik / jumlah_kolom * 100:.2f}%")
print(f"Kategorikal  : {jumlah_kategorikal / jumlah_kolom * 100:.2f}%")

# Tampilkan jumlah nilai unik pada setiap kolom
print("\n=== JUMLAH NILAI UNIK PER KOLOM ===")
for kolom in df.columns:
    print(f"{kolom}: {df[kolom].nunique(dropna=True)} nilai unik")

# 3. ANALISIS DUPLIKAT
jumlah_baris = len(df)
jumlah_duplikat = int(df.duplicated().sum())
persen_duplikat = jumlah_duplikat / jumlah_baris * 100 if jumlah_baris else 0

print("\n=== ANALISIS DUPLIKAT ===")
print(f"Jumlah baris duplikat : {jumlah_duplikat}")
print(f"Persentase duplikat   : {persen_duplikat:.2f}%")

if jumlah_duplikat:
    print("\nContoh baris duplikat:")
    print(df[df.duplicated(keep=False)].head(10))
else:
    print("Tidak ditemukan baris duplikat.")

# 4. ANALISIS DATA KOSONG / NULL
jumlah_null_per_kolom = df.isna().sum()
persen_null_per_kolom = df.isna().mean() * 100

tabel_null = pd.DataFrame({
    "Jumlah_Null": jumlah_null_per_kolom,
    "Persentase_Null": persen_null_per_kolom.round(2)
})

print("\n=== ANALISIS NULL PER KOLOM ===")
print(tabel_null.to_string())

total_null = int(df.isna().sum().sum())
total_sel = df.shape[0] * df.shape[1]
persen_total_null = total_null / total_sel * 100 if total_sel else 0

print(f"\nTotal sel kosong : {total_null}")
print(f"Persentase sel kosong dari seluruh sel : {persen_total_null:.2f}%")

# 5. ANALISIS NILAI NOL PADA KOLOM NUMERIK
# Nilai 0 belum tentu salah; maknanya bergantung pada kolom.
data_zero = []
for kolom in kolom_numerik:
    jumlah_zero = int((df[kolom] == 0).sum())
    persen_zero = jumlah_zero / jumlah_baris * 100 if jumlah_baris else 0
    data_zero.append({
        "Kolom": kolom,
        "Jumlah_Zero": jumlah_zero,
        "Persentase_Zero": round(persen_zero, 2)
    })

tabel_zero = pd.DataFrame(data_zero)

print("\n=== ANALISIS NILAI ZERO ===")
print(tabel_zero.to_string(index=False))

# 6. FREKUENSI DAN PERSENTASE DATA KATEGORIKAL
print("\n=== FREKUENSI DATA KATEGORIKAL ===")
for kolom in kolom_kategorikal:
    print(f"\nKolom: {kolom}")
    frekuensi = df[kolom].value_counts(dropna=False)
    persentase = df[kolom].value_counts(normalize=True, dropna=False) * 100
    hasil = pd.DataFrame({
        "Jumlah": frekuensi,
        "Persentase": persentase.round(2)
    })
    print(hasil.to_string())

# 7. RINGKASAN KUALITAS DATA
ringkasan = pd.DataFrame({
    "Tipe_Data": df.dtypes.astype(str),
    "Jumlah_Null": df.isna().sum(),
    "Persentase_Null": (df.isna().mean() * 100).round(2),
    "Jumlah_Nilai_Unik": df.nunique(dropna=True)
})
ringkasan["Jumlah_Zero"] = [
    int((df[kolom] == 0).sum()) if kolom in kolom_numerik else np.nan
    for kolom in df.columns
]

ringkasan.to_csv("ringkasan_kualitas_brand_fashion.csv", index=True)
print("\nRingkasan kualitas data disimpan ke:")
print("ringkasan_kualitas_brand_fashion.csv")

# 8. CONTOH PENGGUNAAN SCIKIT-LEARN
# LabelEncoder mengubah kategori menjadi angka untuk kebutuhan pemrosesan.
# Data asli df tidak diubah.
df_encoded = df.copy()
encoder = LabelEncoder()

for kolom in kolom_kategorikal:
    nilai_terisi = df_encoded[kolom].notna()
    df_encoded.loc[nilai_terisi, kolom] = encoder.fit_transform(
        df_encoded.loc[nilai_terisi, kolom].astype(str)
    ).astype(str)

print("\n=== CONTOH DATA SETELAH ENCODING KATEGORIKAL ===")
print(df_encoded.head())

# 9. VISUALISASI
# Grafik 1: jumlah kolom numerik dan kategorikal
plt.figure(figsize=(7, 5))
plt.bar(["Numerik", "Kategorikal"], [jumlah_numerik, jumlah_kategorikal])
plt.title("Jumlah Kolom Berdasarkan Jenis Data")
plt.ylabel("Jumlah Kolom")
plt.tight_layout()
plt.show()

# Grafik 2: jumlah null per kolom
plt.figure(figsize=(11, 5))
jumlah_null_per_kolom[jumlah_null_per_kolom > 0].sort_values(
    ascending=False
).plot(kind="bar")
plt.title("Jumlah Data Kosong (Null) per Kolom")
plt.ylabel("Jumlah Null")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Grafik 3: jumlah zero per kolom numerik
plt.figure(figsize=(11, 5))
tabel_zero.set_index("Kolom")["Jumlah_Zero"].plot(kind="bar")
plt.title("Jumlah Nilai Nol pada Kolom Numerik")
plt.ylabel("Jumlah Nilai Nol")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Grafik 4: histogram untuk setiap kolom numerik
if kolom_numerik:
    df[kolom_numerik].hist(figsize=(14, 10), bins=15)
    plt.suptitle("Distribusi Kolom Numerik")
    plt.tight_layout()
    plt.show()

# Grafik 5: distribusi kategori untuk beberapa kolom kategorikal
# Maksimal 10 kategori ditampilkan agar grafik tetap terbaca.
for kolom in kolom_kategorikal:
    frekuensi = df[kolom].value_counts().head(10)
    plt.figure(figsize=(8, 5))
    frekuensi.plot(kind="bar")
    plt.title(f"Distribusi Kategori: {kolom}")
    plt.ylabel("Jumlah Data")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

print("\n=== ANALISIS SELESAI ===")
