# Analisis Dataset Brand Fashion Lokal

## Deskripsi Proyek

Proyek ini merupakan analisis data Brand Fashion Lokal menggunakan Python. Analisis dilakukan untuk mengetahui struktur dataset, mengidentifikasi jenis data, memeriksa kualitas data, serta menampilkan hasil analisis dalam bentuk grafik.

## Tujuan

- Mengidentifikasi jenis data numerik dan kategorikal.
- Menghitung jumlah dan persentase data duplikat.
- Memeriksa data kosong (*null*).
- Memeriksa nilai nol (*zero*) pada kolom numerik.
- Menampilkan statistik deskriptif dan distribusi data.
- Membuat visualisasi untuk membantu memahami dataset.
- Menyimpan ringkasan kualitas data dalam format CSV.

## Tools dan Library

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Struktur Proyek

```text
analisis-brand-fashion/
├── analisis_brand_fashion.py
├── dataset_brand_fashion_lokal.csv
├── ringkasan_kualitas_brand_fashion.csv
└── README.md
```

File `ringkasan_kualitas_brand_fashion.csv` dihasilkan otomatis setelah program dijalankan.

## Dataset

Dataset yang digunakan adalah `dataset_brand_fashion_lokal.csv`, yang berisi data terkait brand fashion lokal.

Pastikan file dataset berada di folder yang sama dengan script Python. Nama file yang digunakan pada program adalah:

```python
PATH_CSV = "dataset_brand_fashion_lokal.csv"
```

## Instalasi Library

Jalankan perintah berikut melalui terminal:

```bash
python -m pip install numpy pandas scikit-learn matplotlib
```

## Cara Menjalankan Program

1. Siapkan file Python dan dataset CSV.
2. Buka terminal pada folder proyek.
3. Jalankan perintah berikut:

```bash
python analisis_brand_fashion.py
```

4. Tunggu sampai proses analisis selesai.
5. Lihat hasil analisis di terminal dan grafik yang ditampilkan.
6. Periksa file CSV ringkasan yang dihasilkan.

## Analisis yang Dilakukan

### 1. Pemeriksaan Dataset
Menampilkan lima data pertama, ukuran dataset, informasi tipe data, dan statistik deskriptif.

### 2. Identifikasi Jenis Data
Memisahkan kolom numerik dan kategorikal serta menghitung persentasenya.

### 3. Pemeriksaan Duplikat
Menghitung jumlah dan persentase baris yang memiliki data duplikat.

### 4. Pemeriksaan Data Kosong
Menghitung jumlah dan persentase nilai kosong pada setiap kolom.

### 5. Pemeriksaan Nilai Nol
Menghitung jumlah nilai nol pada kolom numerik. Nilai nol tidak selalu berarti kesalahan karena perlu disesuaikan dengan konteks data.

### 6. Distribusi Kategorikal
Menampilkan frekuensi dan persentase setiap kategori.

### 7. Visualisasi Data
Membuat grafik jumlah jenis kolom, data kosong, nilai nol, histogram numerik, dan distribusi kategori.

### 8. Encoding Data
Menggunakan `LabelEncoder` dari Scikit-learn sebagai contoh mengubah data kategorikal menjadi representasi angka.

## Output Program

Program menghasilkan:

- Informasi dataset dan statistik deskriptif.
- Hasil pemeriksaan duplikat, null, dan zero.
- Grafik visualisasi data.
- File `ringkasan_kualitas_brand_fashion.csv`.

## Catatan

Proyek ini berfokus pada analisis eksplorasi data (*Exploratory Data Analysis / EDA*) dan pemeriksaan kualitas dataset. Program belum melatih atau mengevaluasi model prediksi pembelian ulang.

## Lisensi

Informasi lisensi dapat ditambahkan sesuai hak penggunaan dataset dan ketentuan proyek.
