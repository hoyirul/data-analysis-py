import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
path_day = './data/day.csv'  # Sesuaikan dengan lokasi file
df = pd.read_csv(path_day)

# Tren Harian Jumlah Sepeda yang Dipinjam Selama Setahun
st.title('Tren Harian Jumlah Sepeda yang Dipinjam Selama Setahun')

# Ubah kolom 'dteday' menjadi tipe data datetime jika belum
df['dteday'] = pd.to_datetime(df['dteday'])

# Visualisasi tren harian jumlah sepeda yang dipinjam
plt.figure(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=df)
plt.title('Tren Harian Jumlah Sepeda yang Dipinjam Selama Setahun')
plt.xlabel('Tanggal')
plt.ylabel('Count')
st.pyplot(plt)

# Kesimpulan Pertanyaan 1
st.subheader('Kesimpulan Pertanyaan 1:')
st.write('Dari visualisasi tren harian jumlah sepeda yang dipinjam selama setahun, terlihat bahwa:')
st.write('- Terdapat fluktuasi yang cukup signifikan dalam jumlah sepeda yang dipinjam dari waktu ke waktu.')
st.write('- Pada beberapa titik tertentu, terlihat lonjakan yang mungkin terkait dengan peristiwa khusus atau musiman tertentu.')

# Korelasi Antara Variabel Cuaca dengan Jumlah Sepeda yang Dipinjam
st.title('Korelasi Antara Variabel Cuaca dengan Jumlah Sepeda yang Dipinjam')

# Visualisasi korelasi antara variabel cuaca ('weathersit') dengan jumlah sepeda yang dipinjam
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=df)
plt.title('Pengaruh Variabel Cuaca terhadap Jumlah Sepeda yang Dipinjam')
plt.xlabel('Weather Situation')
plt.ylabel('Count')
st.pyplot(plt)

# Kesimpulan Pertanyaan 2
st.subheader('Kesimpulan Pertanyaan 2:')
st.write('Dari visualisasi korelasi antara variabel cuaca ("weathersit") dengan jumlah sepeda yang dipinjam, terlihat bahwa:')
st.write('- Saat kondisi cuaca memburuk, jumlah sepeda yang dipinjam cenderung menurun secara signifikan.')
st.write('- Kondisi cuaca yang lebih baik memiliki jumlah sepeda yang dipinjam lebih tinggi.')

# Catatan Akhir
st.title('Catatan Akhir:')
st.write('- Analisis ini memberikan wawasan awal tentang tren harian dan pengaruh kondisi cuaca terhadap jumlah sepeda yang dipinjam.')
st.write('- Namun, untuk pemahaman yang lebih komprehensif, diperlukan analisis yang lebih mendalam serta integrasi faktor-faktor lain yang mungkin memengaruhi pola penggunaan sepeda.')
