import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul halaman
st.title('E-commerce Data Dashboard')
st.write("""
Dashboard ini menampilkan visualisasi dari:
1. Tren penjualan bulanan produk parfum di Sao Paulo selama dua tahun terakhir.
2. Kota besar dengan persentase pengiriman terlambat di atas 15 persen pada tahun 2018.
""")

# Load data yang sudah dikonversi dan dibersihkan
tren_bulanan_sao_paulo = pd.read_csv("tren_bulanan_sao_paulo.csv")
persentase_diatas_15 = pd.read_csv("persentase_diatas_15.csv")

# inisiasi tab yang akan dipakai
tab1, tab2 = st.tabs(["Tren Penjualan Bulanan", "Persentase Pengiriman Terlambat"])

# inisiasi tab 1 yang akan dipakai untuk tren bulanan produk parfum
with tab1:
    st.header("Tren Penjualan Bulanan Produk Parfum di Sao Paulo")

    # Visualisasi Tren Penjualan Bulanan
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(tren_bulanan_sao_paulo['year_month'], tren_bulanan_sao_paulo['jumlah_penjualan'], marker='o', color='b')
    ax1.set_title('Tren Penjualan Bulanan Produk Parfum di Sao Paulo (Dua Tahun Terakhir)')
    ax1.set_xlabel('Bulan')
    ax1.set_ylabel('Jumlah Penjualan')
    ax1.grid(True)
    ax1.set_xticks(range(len(tren_bulanan_sao_paulo['year_month'])))
    ax1.set_xticklabels(tren_bulanan_sao_paulo['year_month'], rotation=45, ha='center')

    # Menambahkan padding agar tidak terpotong
    plt.tight_layout()

    # menampilkan visualisasi
    st.pyplot(fig1)

# inisiasi tab 2 yang akan dipakai untuk persentase pengiriman terlambat
with tab2:
    st.header("Persentase Pengiriman Terlambat di Kota Besar (2018)")

    # Visualisasi Persentase Pengiriman Terlambat
    fig2, ax2 = plt.subplots(figsize=(15, 10))
    persentase_diatas_15 = persentase_diatas_15.sort_values(by='persentase_pengiriman_terlambat', ascending=False)
    ax2.bar(persentase_diatas_15['customer_city'], persentase_diatas_15['persentase_pengiriman_terlambat'], color='r')
    ax2.set_title('Kota Besar Dengan Persentase Pengiriman Terlambat di Atas 15% (2018)')
    ax2.set_xlabel('Kota')
    ax2.set_ylabel('Persentase Pengiriman Terlambat (%)')
    ax2.set_xticklabels(persentase_diatas_15['customer_city'], rotation=90, ha='center')
    ax2.grid(True)

    # Menambahkan padding agar tidak terpotong
    plt.tight_layout()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig2)
