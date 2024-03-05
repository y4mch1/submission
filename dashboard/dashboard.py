import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


df = pd.read_csv('all_data.csv')

pivot_table_pm25 = pd.pivot_table(df, values='PM2.5', index=['year', 'month'], aggfunc='mean').reset_index()
st.title('Analysis Data Project')

st.write("Nama: Widian Sasi Disertasiani")
st.write("Email: m004d4kx2669@bangkit.academy")
st.write("Dicoding ID: widian_ogik")

st.subheader('Qusetions')
st.write("1. Bagaimana peningkatan polusi udara pada tahun 2013 hinga 2015?")
st.write("2. Apakah ada bulan-bulan tertentu yang tingkat polusi udaranya selalu lebih tinggi?")

st.subheader('First Few Dataset')
csv_file= "all_data.csv"
appended_df = pd.read_csv(csv_file)
st.dataframe(appended_df.sample(5))

st.subheader("Deskripsi Data:")
st.write(appended_df.describe())

st.subheader('Description')
features_list = [
    "day: Waktu ketika pengukuran diambil.",
    "hour: Jam ketika pengukuran diambil.",
    "PM2.5: Partikulat matter dengan diameter 2.5 mikrometer atau kurang.",
    "PM10: Partikulat matter dengan diameter 10 mikrometer atau kurang.",
    "SO2: Sulfur Dioksida, gas yang utamanya berasal dari pembakaran bahan bakar fosil.",
    "NO2: Nitrogen Dioksida, gas yang utamanya berasal dari pembakaran bahan bakar fosil.",
    "CO: Karbon Monoksida, gas tanpa warna dan bau yang dihasilkan dari pembakaran tidak sempurna bahan bakar berkarbon.",
    "O3: Ozon, polutan udara berbahaya saat dihirup.",
    "TEMP: Suhu.",
    "PRES: Tekanan.",
    "DEWP: Titik embun.",
    "RAIN: Curah hujan.",
    "wd: Arah Angin.",
    "WSPM: Kecepatan Angin.",
    "station: Pengidentifikasi stasiun."
]

for feature in features_list:
    st.write(f"- {feature}")
    


st.subheader('Peningkatan Polusi Udara (PM2.5) per Tahun')
line_chart = sns.lineplot(data=pivot_table_pm25, x='year', y='PM2.5')
st.pyplot(line_chart.figure)

st.subheader('Statistik polusi udara pada tiap bulan')
# Pivot table untuk melihat rata-rata PM2.5 per bulan
pivot_table_monthly = pd.pivot_table(appended_df, values='PM2.5', index='month', aggfunc='mean').reset_index()

# Sorting pivot table berdasarkan rata-rata PM2.5
pivot_table_monthly = pivot_table_monthly.sort_values(by='PM2.5', ascending=False)

# Visualisasi bar chart
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=pivot_table_monthly, x='month', y='PM2.5', palette='viridis')
plt.title('Rata-rata Polusi Udara (PM2.5) per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata PM2.5')
st.pyplot(fig)


st.subheader('HeatMap')
# Pilih kolom yang ingin diambil untuk heatmap
selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

# Hitung matriks korelasi antar kolom terpilih
correlation_matrix = appended_df[selected_columns].corr()

# Plot heatmap
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
plt.title('Heatmap')
st.pyplot(fig)

st.write("Dalam dataset ini, terlihat adanya hubungan erat antara beberapa variabel. Beberapa temuan menarik mencakup:")
st.write("1. Partikel Udara (PM2.5 dan PM10): Terdapat korelasi tinggi antara kandungan PM2.5 dan PM10, menunjukkan bahwa kedua jenis partikel tersebut cenderung berasal dari sumber yang sama.")
st.write("2. Partikel Udara (PM2.5/PM10) dan CO: Korelasi positif antara rasio PM2.5/PM10 dan kandungan CO menunjukkan adanya potensi polutan bersumber dari sumber yang sama.")
st.write("3. Suhu (TEMP), Tekanan Udara (PRES), dan Titik Embun (DEWP): Variabel-variabel ini menunjukkan korelasi, menunjukkan bahwa perubahan suhu dapat memengaruhi tekanan udara dan titik embun.")
st.write("4. CO dan NO2: Terdapat korelasi antara kandungan CO dan NO2, mengindikasikan kemungkinan hubungan antara dua jenis polutan ini.")

st.subheader('Kesimpulan')
st.write("1.Selama periode 2013-2015, kita dapat mengamati tren penurunan yang cukup stabil dalam tingkat polusi udara, khususnya PM2.5. Pada awal periode, tingkat PM2.5 mencapai angka sekitar 100 dan kemudian secara konsisten mengalami penurunan hingga mencapai sekitar 80 pada pertengahan tahun 2015. Namun, setelah tahun 2015, kita melihat adanya perubahan tren yang signifikan Terjadi peningkatan tajam dalam tingkat polusi udara, dan pada pertengahan tahun 2017, tingkat PM2.5 bahkan melampaui angka sebelum penurunan pada tahun 2015. Kondisi ini menunjukkan bahwa setelah periode penurunan yang stabil, terjadi fluktuasi yang signifikan dan peningkatan kembali dalam tingkat polusi udara, yang memerlukan perhatian khusus dalam pemantauan dan pengelolaan kualitas udara di wilayah tersebut.")
st.write("2.Berdasarkan analisis grafik, dapat disimpulkan bahwa tidak terdapat pola konsisten dari bulan ke bulan di mana tingkat polusi udara selalu lebih tinggi. Meskipun demikian, dari data yang ada, terlihat bahwa bulan Januari dan Februari cenderung memiliki tingkat polusi udara yang paling tinggi. Hal ini dapat menunjukkan adanya faktor-faktor tertentu, seperti kondisi cuaca atau pola emisi, yang berkontribusi pada peningkatan polusi udara pada periode tersebut.")