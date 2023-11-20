import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path_day = './data/day.csv'
df = pd.read_csv(path_day)
df['dteday'] = pd.to_datetime(df['dteday'])

st.sidebar.title('Tren Harian Jumlah Sepeda yang Dipinjam')
plt.figure(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=df)
st.pyplot(plt)

st.sidebar.subheader('Kesimpulan Pertanyaan 1:')
st.sidebar.write('- Fluktuasi signifikan dalam jumlah sepeda.')
st.sidebar.write('- Lonjakan terkait peristiwa khusus/musiman.')

st.sidebar.title('Korelasi Cuaca dengan Jumlah Sepeda')
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=df)
st.pyplot(plt)

st.sidebar.subheader('Kesimpulan Pertanyaan 2:')
st.sidebar.write('- Cuaca buruk = penurunan peminjaman sepeda.')
st.sidebar.write('- Cuaca baik = lebih banyak peminjaman.')

st.sidebar.title('Catatan Akhir:')
st.sidebar.write('- Analisis memberi wawasan awal.')
st.sidebar.write('- Perlu analisis lebih mendalam.')