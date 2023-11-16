# Analisis Data Sepeda

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data sepeda terkait tren harian penggunaan sepeda dan pengaruh kondisi cuaca terhadap jumlah sepeda yang dipinjam.

## Dataset
Dataset yang digunakan dapat ditemukan di `day.csv` dan berisi informasi harian tentang penggunaan sepeda.

## Langkah-Langkah Analisis
1. **Gathering Data**: Memuat data dari `day.csv`.
2. **Exploratory Data Analysis (EDA)**:
    - Menganalisis tren harian jumlah sepeda yang dipinjam selama setahun.
    - Membuat visualisasi terkait korelasi antara variabel cuaca dan jumlah sepeda yang dipinjam.
3. **Kesimpulan**:
    - Meringkas temuan dari analisis tren harian dan pengaruh kondisi cuaca terhadap jumlah sepeda yang dipinjam.

## Dashboard Analisis Data Sepeda

## Cara Menjalankan Aplikasi
1. Pastikan Anda telah menginstal Python dan Streamlit.
2. Unduh proyek ini ke dalam direktori lokal.
3. Buka terminal atau command prompt, dan navigasi ke direktori proyek.
4. Jalankan perintah berikut: (`streamlit run dashboard/dashboard.py`)
5. Setelah menjalankan perintah tersebut, Anda akan melihat URL lokal yang dapat Anda salin dan tempel ke browser untuk melihat dashboard analisis data sepeda.

## Struktur Proyek
- `dashboard/`: Direktori yang berisi kode aplikasi Streamlit.
- `dashboard.py`: Kode aplikasi Streamlit untuk menampilkan analisis data.
- `day.csv`: Dataset utama.
- `README.md`: Dokumentasi proyek.

## Catatan Penting
Pastikan bahwa `day.csv` terletak dalam direktori yang sama dengan `dashboard.py` agar aplikasi dapat berjalan dengan baik. Aplikasi ini memberikan gambaran visual tentang tren harian penggunaan sepeda dan pengaruh kondisi cuaca terhadap jumlah sepeda yang dipinjam berdasarkan analisis yang telah dilakukan sebelumnya.

---
Jalankan aplikasi Streamlit ini untuk melihat visualisasi dan kesimpulan dari analisis data sepeda yang telah dilakukan sebelumnya.

## File
- `day.csv`: Data harian tentang penggunaan sepeda.

## Struktur Proyek
- `README.md`: Dokumentasi proyek.
- `day.csv`: Dataset utama.
- `analisis.py`: Kode Python untuk analisis data menggunakan Streamlit.

## Penggunaan
1. Pastikan Python dan Streamlit sudah terinstal.
2. Jalankan perintah `streamlit run analisis.py` untuk melihat analisis data dalam bentuk aplikasi Streamlit.

## Catatan Akhir
Analisis ini memberikan gambaran awal tentang pola penggunaan sepeda berdasarkan tren harian dan faktor cuaca. Untuk pemahaman yang lebih dalam, diperlukan analisis tambahan dan integrasi faktor-faktor lain yang mungkin memengaruhi pola penggunaan sepeda.
