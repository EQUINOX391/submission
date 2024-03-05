import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import altair as alt
import numpy as np
from babel.numbers import format_currency
import plotly.figure_factory as ff
from vega_datasets import data
import pydeck as pdk
sb.set(style='dark')

# Function to load sorted_df_cat
@st.cache_data
def load_sorted_df_cat():
    sorted_df_cat = pd.read_csv("dashboard/sorted_df_cat.csv")
    return sorted_df_cat

# Function to load sum_spend_df
@st.cache_data
def load_sum_spend_df():
    sum_spend_df = pd.read_csv("dashboard/sum_spend_df.csv")
    return sum_spend_df

# Function to load buy_df
@st.cache_data
def load_buy_df():
    buy_df = pd.read_csv("dashboard/buy_df.csv")
    return buy_df

# Function to load top_products
@st.cache_data
def load_top_products():
    top_products = pd.read_csv("dashboard/top_products.csv")
    return top_products

# Function to load customers_state
@st.cache_data
def load_customers_state():
    customers_state = pd.read_csv("dashboard/customers_state.csv")
    return customers_state

# Function to load customers_city
@st.cache_data
def load_customers_city():
    customers_city = pd.read_csv("dashboard/customers_city.csv")
    return customers_city

# Function to load customers_city_top30
@st.cache_data
def load_customers_city_top30():
    customers_city_top30 = pd.read_csv("dashboard/customers_city_top30.csv")
    return customers_city_top30

# Function to load customers_loc
@st.cache_data
def load_customers_loc():
    customers_loc = pd.read_csv("dashboard/customers_loc.csv")
    return customers_loc

# Function to load rfm_df
@st.cache_data
def load_rfm_df():
    rfm_df = pd.read_csv("dashboard/rfm_df.csv")
    return rfm_df

# Function to load segment_df
@st.cache_data
def load_segment_df():
    segment_df = pd.read_csv("dashboard/segment_df.csv")
    return segment_df

# Function to load rank_df
@st.cache_data
def load_rank_df():
    rank_df = pd.read_csv("dashboard/rank_df.csv")
    return rank_df

def main():
    sorted_df_cat = load_sorted_df_cat()
    sum_spend_df = load_sum_spend_df()
    buy_df = load_buy_df()
    top_products = load_top_products()
    customers_state = load_customers_state()
    customers_city = load_customers_city()
    customers_city_top30 = load_customers_city_top30()
    customers_loc = load_customers_loc()
    rfm_df = load_rfm_df()
    segment_df = load_segment_df()
    rank_df = load_rank_df()

    with st.sidebar:
        # Menambahkan logo perusahaan
        st.image("https://valorcapitalgroup.com/wp-content/uploads/2020/06/3f49143da00cfc426e7a27ba908e9c0a-removebg-preview-1-removebg-preview.png")
    st.sidebar.header("**Egi Erlangga's Analysis**")
    selected_diagram = st.sidebar.selectbox("Pilih Visualisasi", ("Home", "All In One", "Tren Belanja Pelanggan", "Persebaran Tempat Tinggal Pelanggan", "RFM Analysis","Segmentasi Pelanggan"))


    # Show all plots in one page
    if selected_diagram == "Home":
      st.title("Dashboard Data Olist Analysis")
      st.header("Dicoding Project : Data Analysis With Python")
      st.caption("Oleh Egi Erlangga | EQUINOX391 | egimon391@gmail.com")
      st.header("")
      st.header("Tentang Dataset Ini")

      # Streamlit Header
      st.subheader("Dataset E-Commerce Brazil oleh Olist")
      st.caption("Selamat datang! Ini adalah dataset e-commerce Brasil dari pesanan yang dibuat di Toko Olist. Dataset ini berisi informasi tentang 100 ribu pesanan dari tahun 2016 hingga 2018 yang dibuat di berbagai pasar di Brasil.")
      st.caption("Fitur dataset ini memungkinkan untuk melihat suatu pesanan dari berbagai dimensi: dari status pesanan, harga, pembayaran, dan kinerja pengiriman hingga lokasi pelanggan, atribut produk, dan ulasan yang ditulis oleh pelanggan.")

      # Streamlit Link
      st.markdown("[Link Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")  # Ganti '#' dengan tautan dataset yang sesuai

      # Streamlit Header
      st.subheader("Gabungkan dengan Funnel Pemasaran oleh Olist")
      st.caption("Kami juga telah merilis dataset Funnel Pemasaran. Anda dapat menggabungkan kedua dataset ini dan melihat pesanan dari perspektif pemasaran sekarang!")

      # Streamlit Link
      st.markdown("[Petunjuk Penggabungan](https://www.kaggle.com/olistbr/marketing-funnel-olist/home)")  # Ganti '#' dengan tautan petunjuk penggabungan yang sesuai

      # Streamlit Text
      st.subheader("Konteks")
      st.caption("Dataset ini disediakan dengan murah hati oleh Olist, toko departemen terbesar di pasar e-commerce Brasil. Olist menghubungkan bisnis kecil dari seluruh Brasil ke saluran tanpa kerumitan dan dengan satu kontrak tunggal.")

      # Streamlit Link
      st.markdown("[Lihat lebih lanjut di situs web kami](https://www.olist.com)")  # Ganti tautan dengan tautan situs web yang sesuai

      # Streamlit Text
      st.caption("Setelah pelanggan membeli produk dari Toko Olist, penjual diberi tahu untuk memenuhi pesanan tersebut. Setelah pelanggan menerima produk atau tanggal pengiriman perkiraan tiba, pelanggan mendapatkan survei kepuasan melalui email di mana mereka dapat memberikan penilaian untuk pengalaman pembelian dan menulis beberapa komentar.")

      # Streamlit Alert
      st.warning("**Perhatian**: Sebuah pesanan mungkin memiliki beberapa item. Setiap item mungkin dipenuhi oleh penjual yang berbeda. Semua teks yang mengidentifikasi toko dan mitra diganti dengan nama-nama keluarga besar Game of Thrones.")

      # Streamlit Header
      st.header("Skema Data")

      # Streamlit Image
      st.image("https://i.imgur.com/HRhd2Y0.png")  # Ganti 'link_gambar_skema_data.png' dengan tautan gambar skema data yang sesuai

      # Streamlit Header
      st.header("Inspirasi")

      # Streamlit Text
      st.caption("Berikut adalah beberapa inspirasi untuk hasil yang mungkin dari dataset ini.")

      # Streamlit Bulleted List
      st.markdown("- **NLP:** Dataset ini menawarkan lingkungan luar biasa untuk mengurai teks ulasan melalui berbagai dimensinya.")
      st.markdown("- **Pengelompokan:** Beberapa pelanggan tidak menulis ulasan. Tapi mengapa mereka senang atau marah?")
      st.markdown("- **Prediksi Penjualan:** Dengan informasi tanggal pembelian, Anda akan dapat memprediksi penjualan di masa depan.")
      st.markdown("- **Kinerja Pengiriman:** Anda juga akan dapat bekerja melalui kinerja pengiriman dan menemukan cara untuk mengoptimalkan waktu pengiriman.")
      st.markdown("- **Kualitas Produk:** Nikmati menemukan kategori produk yang lebih rentan terhadap ketidakpuasan pelanggan.")
      st.markdown("- **Rekayasa Fitur:** Buat fitur dari dataset kaya ini atau lampirkan beberapa informasi publik eksternal ke dalamnya.")

      # Streamlit Header
      st.header("Pengakuan Terima Kasih")

      # Streamlit Text
      st.caption("Terima kasih kepada Olist karena telah mempublikasikan dataset ini.")

    else:
      # Individual plots
      if selected_diagram == "All In One":
        st.title('Menampilkan Seluruh Diagram')

        #Populer vs tidak populer
        st.header("Produk Paling Populer")
        st.caption("Diagram ini menunjukkan 10 produk yang paling populer tiap bulannya selama rentang waktu perekaman data berlangsung")
        chart_populer = alt.Chart(sorted_df_cat.head(10)).mark_bar().encode(
            x=alt.X("product_id:Q", title="Product ID"),
            y=alt.Y("product_category_name_english:N", title="Product Category", sort="-x"),  # Sorting by order_id in descending order
            color=alt.Color("product_id:Q", scale=alt.Scale(scheme="reds")),
            tooltip=["product_id"],
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(chart_populer, use_container_width=True)


        st.header("Produk Paling Tidak Populer")
        st.caption("Diagram ini menunjukkan 10 produk yang paling tidak populer tiap bulannya selama rentang waktu perekaman data berlangsung")
        chart_tidakpopuler = alt.Chart(sorted_df_cat.tail(10)).mark_bar().encode(
            x=alt.X("product_id:Q", title="Product ID"),
            y=alt.Y("product_category_name_english:N", title="Product Category", sort="x"),  # Sorting by order_id in descending order
            color=alt.Color("product_id:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["product_id"],
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(chart_tidakpopuler, use_container_width=True)

        #Belanja Per Bulan
        st.header("Total Belanja Pelanggan Perbulan")
        st.caption("Diagram ini menunjukkan kebiasaan belanja pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Dapatkan 5 bulan teratas berdasarkan total pengeluaran
        top5_months = sum_spend_df.groupby('order_approved_at')['total_spend'].sum().nlargest(5).index
        # Buat kolom baru 'top5' untuk menentukan apakah suatu bulan ada di 5 teratas atau tidak
        sum_spend_df['Penjelasan'] = sum_spend_df['order_approved_at'].isin(top5_months)
        # Buat chart
        chart_spend = alt.Chart(sum_spend_df).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan",sort=None),
            y=alt.Y("total_spend:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("Penjelasan:N", scale=alt.Scale(domain=[True, False], range=['#FF6F61', '#D3D3D3'])),
            tooltip=["order_approved_at:N", "total_spend:Q"]
        ).properties(
            width=600,
            height=300,
            title="Top 5 Bulan Terbanyak Belanja Pelanggan"
        )
        # Tampilkan chart
        st.altair_chart(chart_spend, use_container_width=True)

        #Belanja Per Bulan
        st.header("Total Pesanan Produk Perbulan")
        st.caption("Diagram ini menunjukkan banyaknya pesanan barang tiap bulannya selama rentang waktu perekaman data")
        # Dapatkan 5 bulan teratas berdasarkan total pengeluaran
        top5_months_buy = buy_df.groupby('order_approved_at')['total_buy'].sum().nlargest(5).index
        # Buat kolom baru 'top5' untuk menentukan apakah suatu bulan ada di 5 teratas atau tidak
        buy_df['Penjelasan'] = buy_df['order_approved_at'].isin(top5_months_buy)
        # Buat chart
        chart_buy = alt.Chart(buy_df).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan",sort=None),
            y=alt.Y("total_buy:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("Penjelasan:N", scale=alt.Scale(domain=[True, False], range=['#FF6F61', '#D3D3D3'])),
            tooltip=["order_approved_at:N", "total_sbuy:Q"]
        ).properties(
            width=600,
            height=300,
            title="Top 5 Bulan Terbanyak Belanja Pelanggan"
        )
        # Tampilkan chart
        st.altair_chart(chart_buy, use_container_width=True)


        st.header("Total Pesanan Barang Perbulan")
        st.caption("Diagram ini menunjukkan banyaknya total pesanan pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Buat chart
        chart_buy_line = alt.Chart(buy_df).mark_line().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("total_buy:Q", title="Total Order Pelanggan"),
            color=alt.value('#FF6F61'),  # Mengatur warna garis menjadi warna tertentu
            tooltip=["order_approved_at:N", "total_buy:Q"]
        ).properties(
            width=600,
            height=300,
        )

        # Tampilkan chart
        st.altair_chart(chart_buy_line, use_container_width=True)

        st.header("Total Belanja Pelanggan Perbulan")
        st.caption("Diagram ini menunjukkan kebiasaan belanja pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Buat chart
        chart_spend_line = alt.Chart(sum_spend_df).mark_line().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("total_spend:Q", title="Total Belanja Pelanggan"),
            color=alt.value('blue'),  # Mengatur warna garis menjadi warna tertentu
            tooltip=["order_approved_at:N", "total_spend:Q"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(chart_spend_line, use_container_width=True)


        # Chart Kategori Produk Terlaris
        # Buat chart
        st.header("Produk Terpopuler Setiap Bulannya")
        st.caption("Diagram ini menunjukkan tren produk populer tiap bulannya selama rentang waktu perekaman data")
        chart_popular_catt_mon = alt.Chart(top_products).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("product_id:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("product_category_name_english:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["order_approved_at:N", "product_category_name_english:N"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(chart_popular_catt_mon, use_container_width=True)


        # Chart Pengguna State
        # Buat chart
        st.header("Pelanggan Tiap Negara Bagian")
        st.caption("Diagram ini menunjukkan banyaknnya pelanggan di tiap negara bagian")
        customer_state_chart = alt.Chart(customers_state).mark_bar().encode(
            x=alt.X("customer_state", title="Negara Bagian", sort=None),
            y=alt.Y("customers_each_state:Q", title="Banyak Pelanggan"),
            color=alt.Color("customer_state:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["customer_state:N", "customer_each_state:N"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(customer_state_chart, use_container_width=True)


        # Chart Pengguna State
        # Buat chart
        # Batasi data untuk hanya 20 kota pertama
        st.header("Pelanggan Tiap Kota")
        st.caption("Diagram ini menunjukkan banyaknnya pelanggan di 20 kota dengan pelanggan terbanyak")
        filtered_customers_city = customers_city.head(20)

        # Buat chart
        customer_city_chart = alt.Chart(filtered_customers_city).mark_bar().encode(
            x=alt.X("customer_city", title="Negara Bagian", sort=None),
            y=alt.Y("customers_each_city:Q", title="Banyak Pelanggan"),
            color=alt.Color("customer_city:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["customer_city:N", "customer_each_city:N"]
        ).properties(
            width=600,
            height=300,
            title="Pelanggan Tiap Kota"
        )
        st.altair_chart(customer_city_chart, use_container_width=True)

        st.header("Persebaran Pelanggan")
        st.caption("Diagram plot map ini menunjukkan persebaran pelanggan di seluruh negara selama data direkam")
        st.map(data=customers_loc, latitude='geolocation_lat', longitude='geolocation_lng', color='#BB7700', size=1, zoom=None, use_container_width=True)


        st.header("Analisa RFM")
        st.caption("Diagram ini menunjukkan persebaran pola Resensi, Frekuensi, dan Moneter pelanggan")
        # Add histogram data
        r = rfm_df['R']
        f = rfm_df['F']
        m = rfm_df['M']
        # Group data together
        hist_data = [r, f, m]
        group_labels = ['Recency', 'Frequency', 'Monetary']
        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])
        # Plot!
        st.plotly_chart(fig, use_container_width=True)


        # Create a 2x2 grid of subplots
        st.header("Plot 3D Persebaran Pelanggan Berdasarkan RFM")
        st.caption("Diagram ini menunjukkan visualisasi berbeda untuk menggambarkan analisa RFM")
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), subplot_kw={'projection': '3d'})

        # Front view
        axes[0, 0].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[0, 0].set_title('Monetary vs Frequency')
        axes[0, 0].view_init(elev=0, azim=0)

        # Side view
        axes[0, 1].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[0, 1].set_title('Recency vs Frequency')
        axes[0, 1].view_init(elev=90, azim=0)

        # Top view
        axes[1, 0].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[1, 0].set_title('Recency vs Monetary')
        axes[1, 0].view_init(elev=0, azim=90)

        # Neutral view
        axes[1, 1].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[1, 1].set_title('Recency vs Monetary vs Frequency')
        axes[1, 1].view_init(elev=45, azim=45)  # Adjust for a more natural perspective

        # Add labels and colorbar only to the first subplot
        axes[0, 0].set_ylabel('Frequency (number of orders)')
        axes[0, 0].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[0, 0].collections[0], ax=axes[0, 0], label='RFM Score')

        axes[0, 1].set_xlabel('Recency (days)')
        axes[0, 1].set_ylabel('Frequency (number of orders)')
        fig.colorbar(axes[0, 1].collections[0], ax=axes[0, 1], label='RFM Score')

        axes[1, 0].set_xlabel('Recency (days)')
        axes[1, 0].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[1, 0].collections[0], ax=axes[1, 0], label='RFM Score')

        axes[1, 1].set_xlabel('Recency (days)')
        axes[1, 1].set_ylabel('Frequency (number of orders)')
        axes[1, 1].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[1, 1].collections[0], ax=axes[1, 1], label='RFM Score')

        # Convert the Matplotlib figure to a Streamlit image
        st.pyplot(fig)


        # Buat chart
        st.header("Segmentasi Pelanggan")
        st.caption("Diagram ini menunjukkan pengelompokan pelanggan yang dilakukan lewat perilakunya berdasarkan RFM")
        customer_category = alt.Chart(segment_df).mark_bar().encode(
            x=alt.X("Segment:N", title="Segmentasi", sort=None),
            y=alt.Y("Segment_Total_Customer:Q", title="Banyak Pelanggan"),
            color=alt.Color("Segment:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["Segment:N", "Segment_Total_Customer:Q"]
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(customer_category, use_container_width=True)

        # Buat chart
        st.header("Kategorisasi Pelanggan")
        st.caption("Diagram ini menunjukkan bagaimana pelanggan dikategorisasi menjadi rank berdasarkan jumlah skor RFM")

        # Create a pie chart using Matplotlib
        fig, ax = plt.subplots()
        ax.pie(rank_df['Rank_Total_Customer'], labels=rank_df['Rank'], autopct='%1.1f%%', startangle=90, colors=['#FF00FF', '#00BFFF', '#008000', '#C0C0C0', '#FF0000'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart in Streamlit
        st.pyplot(fig)

      elif selected_diagram == "Tren Belanja Pelanggan":
        st.title('Menampilkan Diagram Terkait Tren')
        #Populer vs tidak populer
        st.header("Produk Paling Populer")
        st.caption("Diagram ini menunjukkan 10 produk yang paling populer tiap bulannya selama rentang waktu perekaman data berlangsung")
        chart_populer = alt.Chart(sorted_df_cat.head(10)).mark_bar().encode(
            x=alt.X("product_id:Q", title="Product ID"),
            y=alt.Y("product_category_name_english:N", title="Product Category", sort="-x"),  # Sorting by order_id in descending order
            color=alt.Color("product_id:Q", scale=alt.Scale(scheme="reds")),
            tooltip=["product_id"],
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(chart_populer, use_container_width=True)


        st.header("Produk Paling Tidak Populer")
        st.caption("Diagram ini menunjukkan 10 produk yang paling tidak populer tiap bulannya selama rentang waktu perekaman data berlangsung")
        chart_tidakpopuler = alt.Chart(sorted_df_cat.tail(10)).mark_bar().encode(
            x=alt.X("product_id:Q", title="Product ID"),
            y=alt.Y("product_category_name_english:N", title="Product Category", sort="x"),  # Sorting by order_id in descending order
            color=alt.Color("product_id:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["product_id"],
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(chart_tidakpopuler, use_container_width=True)

        #Belanja Per Bulan
        st.header("Total Belanja Pelanggan Perbulan")
        st.caption("Diagram ini menunjukkan kebiasaan belanja pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Dapatkan 5 bulan teratas berdasarkan total pengeluaran
        top5_months = sum_spend_df.groupby('order_approved_at')['total_spend'].sum().nlargest(5).index
        # Buat kolom baru 'top5' untuk menentukan apakah suatu bulan ada di 5 teratas atau tidak
        sum_spend_df['Penjelasan'] = sum_spend_df['order_approved_at'].isin(top5_months)
        # Buat chart
        chart_spend = alt.Chart(sum_spend_df).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan",sort=None),
            y=alt.Y("total_spend:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("Penjelasan:N", scale=alt.Scale(domain=[True, False], range=['#FF6F61', '#D3D3D3'])),
            tooltip=["order_approved_at:N", "total_spend:Q"]
        ).properties(
            width=600,
            height=300,
            title="Top 5 Bulan Terbanyak Belanja Pelanggan"
        )
        # Tampilkan chart
        st.altair_chart(chart_spend, use_container_width=True)

        #Belanja Per Bulan
        st.header("Total Pesanan Produk Perbulan")
        st.caption("Diagram ini menunjukkan banyaknya pesanan barang tiap bulannya selama rentang waktu perekaman data")
        # Dapatkan 5 bulan teratas berdasarkan total pengeluaran
        top5_months_buy = buy_df.groupby('order_approved_at')['total_buy'].sum().nlargest(5).index
        # Buat kolom baru 'top5' untuk menentukan apakah suatu bulan ada di 5 teratas atau tidak
        buy_df['Penjelasan'] = buy_df['order_approved_at'].isin(top5_months_buy)
        # Buat chart
        chart_buy = alt.Chart(buy_df).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan",sort=None),
            y=alt.Y("total_buy:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("Penjelasan:N", scale=alt.Scale(domain=[True, False], range=['#FF6F61', '#D3D3D3'])),
            tooltip=["order_approved_at:N", "total_sbuy:Q"]
        ).properties(
            width=600,
            height=300,
            title="Top 5 Bulan Terbanyak Belanja Pelanggan"
        )
        # Tampilkan chart
        st.altair_chart(chart_buy, use_container_width=True)


        st.header("Total Pesanan Barang Perbulan")
        st.caption("Diagram ini menunjukkan banyaknya total pesanan pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Buat chart
        chart_buy_line = alt.Chart(buy_df).mark_line().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("total_buy:Q", title="Total Order Pelanggan"),
            color=alt.value('#FF6F61'),  # Mengatur warna garis menjadi warna tertentu
            tooltip=["order_approved_at:N", "total_buy:Q"]
        ).properties(
            width=600,
            height=300,
        )

        # Tampilkan chart
        st.altair_chart(chart_buy_line, use_container_width=True)

        st.header("Total Belanja Pelanggan Perbulan")
        st.caption("Diagram ini menunjukkan kebiasaan belanja pelanggan tiap bulannya selama rentang waktu perekaman data")
        # Buat chart
        chart_spend_line = alt.Chart(sum_spend_df).mark_line().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("total_spend:Q", title="Total Belanja Pelanggan"),
            color=alt.value('blue'),  # Mengatur warna garis menjadi warna tertentu
            tooltip=["order_approved_at:N", "total_spend:Q"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(chart_spend_line, use_container_width=True)


        # Chart Kategori Produk Terlaris
        # Buat chart
        st.header("Produk Terpopuler Setiap Bulannya")
        st.caption("Diagram ini menunjukkan tren produk populer tiap bulannya selama rentang waktu perekaman data")
        chart_popular_catt_mon = alt.Chart(top_products).mark_bar().encode(
            x=alt.X("order_approved_at:N", title="Bulan", sort=None),
            y=alt.Y("product_id:Q", title="Total Belanja Pelanggan"),
            color=alt.Color("product_category_name_english:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["order_approved_at:N", "product_category_name_english:N"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(chart_popular_catt_mon, use_container_width=True)


      elif selected_diagram == "Persebaran Tempat Tinggal Pelanggan":
        st.title('Menampilkan Diagram Terkait Persebaran Daerah Asal Pelanggan')
        # Chart Pengguna State
        # Buat chart
        st.header("Pelanggan Tiap Negara Bagian")
        st.caption("Diagram ini menunjukkan banyaknnya pelanggan di tiap negara bagian")
        customer_state_chart = alt.Chart(customers_state).mark_bar().encode(
            x=alt.X("customer_state", title="Negara Bagian", sort=None),
            y=alt.Y("customers_each_state:Q", title="Banyak Pelanggan"),
            color=alt.Color("customer_state:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["customer_state:N", "customer_each_state:N"]
        ).properties(
            width=600,
            height=300,
        )
        # Tampilkan chart
        st.altair_chart(customer_state_chart, use_container_width=True)


        # Chart Pengguna State
        # Buat chart
        # Batasi data untuk hanya 20 kota pertama
        st.header("Pelanggan Tiap Kota")
        st.caption("Diagram ini menunjukkan banyaknnya pelanggan di 20 kota dengan pelanggan terbanyak")
        filtered_customers_city = customers_city.head(20)

        # Buat chart
        customer_city_chart = alt.Chart(filtered_customers_city).mark_bar().encode(
            x=alt.X("customer_city", title="Negara Bagian", sort=None),
            y=alt.Y("customers_each_city:Q", title="Banyak Pelanggan"),
            color=alt.Color("customer_city:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["customer_city:N", "customer_each_city:N"]
        ).properties(
            width=600,
            height=300,
            title="Pelanggan Tiap Kota"
        )
        st.altair_chart(customer_city_chart, use_container_width=True)

        st.header("Persebaran Pelanggan")
        st.caption("Diagram plot map ini menunjukkan persebaran pelanggan di seluruh negara selama data direkam")
        st.map(data=customers_loc, latitude='geolocation_lat', longitude='geolocation_lng', color='#BB7700', size=1, zoom=None, use_container_width=True)

      elif selected_diagram == "RFM Analysis":
        st.title('Menampilkan RFM analysis Diagram')
        st.header("Analisa RFM")
        st.caption("Diagram ini menunjukkan persebaran pola Resensi, Frekuensi, dan Moneter pelanggan")
        # Add histogram data
        r = rfm_df['R']
        f = rfm_df['F']
        m = rfm_df['M']
        # Group data together
        hist_data = [r, f, m]
        group_labels = ['Recency', 'Frequency', 'Monetary']
        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])
        # Plot!
        st.plotly_chart(fig, use_container_width=True)


        # Create a 2x2 grid of subplots
        st.header("Plot 3D Persebaran Pelanggan Berdasarkan RFM")
        st.caption("Diagram ini menunjukkan visualisasi berbeda untuk menggambarkan analisa RFM")
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), subplot_kw={'projection': '3d'})

        # Front view
        axes[0, 0].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[0, 0].set_title('Monetary vs Frequency')
        axes[0, 0].view_init(elev=0, azim=0)

        # Side view
        axes[0, 1].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[0, 1].set_title('Recency vs Frequency')
        axes[0, 1].view_init(elev=90, azim=0)

        # Top view
        axes[1, 0].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[1, 0].set_title('Recency vs Monetary')
        axes[1, 0].view_init(elev=0, azim=90)

        # Neutral view
        axes[1, 1].scatter(rfm_df['recency'], rfm_df['frequency'], rfm_df['monetary'], c=rfm_df['Total Score'], cmap='hsv', alpha=0.7)
        axes[1, 1].set_title('Recency vs Monetary vs Frequency')
        axes[1, 1].view_init(elev=45, azim=45)  # Adjust for a more natural perspective

        # Add labels and colorbar only to the first subplot
        axes[0, 0].set_ylabel('Frequency (number of orders)')
        axes[0, 0].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[0, 0].collections[0], ax=axes[0, 0], label='RFM Score')

        axes[0, 1].set_xlabel('Recency (days)')
        axes[0, 1].set_ylabel('Frequency (number of orders)')
        fig.colorbar(axes[0, 1].collections[0], ax=axes[0, 1], label='RFM Score')

        axes[1, 0].set_xlabel('Recency (days)')
        axes[1, 0].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[1, 0].collections[0], ax=axes[1, 0], label='RFM Score')

        axes[1, 1].set_xlabel('Recency (days)')
        axes[1, 1].set_ylabel('Frequency (number of orders)')
        axes[1, 1].set_zlabel('Monetary (total purchase value)')
        fig.colorbar(axes[1, 1].collections[0], ax=axes[1, 1], label='RFM Score')

        # Convert the Matplotlib figure to a Streamlit image
        st.pyplot(fig)


      elif selected_diagram == "Segmentasi Pelanggan":
        st.Title('Menampilkan Diagram Terkait Segmentasi')
        # Buat chart
        st.header("Segmentasi Pelanggan")
        st.caption("Diagram ini menunjukkan pengelompokan pelanggan yang dilakukan lewat perilakunya berdasarkan RFM")
        customer_category = alt.Chart(segment_df).mark_bar().encode(
            x=alt.X("Segment:N", title="Segmentasi", sort=None),
            y=alt.Y("Segment_Total_Customer:Q", title="Banyak Pelanggan"),
            color=alt.Color("Segment:N", scale=alt.Scale(scheme="rainbow")),
            tooltip=["Segment:N", "Segment_Total_Customer:Q"]
        ).properties(
            width=600,
            height=300,
        )
        st.altair_chart(customer_category, use_container_width=True)

        # Buat chart
        st.header("Kategorisasi Pelanggan")
        st.caption("Diagram ini menunjukkan bagaimana pelanggan dikategorisasi menjadi rank berdasarkan jumlah skor RFM")

        # Create a pie chart using Matplotlib
        fig, ax = plt.subplots()
        ax.pie(rank_df['Rank_Total_Customer'], labels=rank_df['Rank'], autopct='%1.1f%%', startangle=90, colors=['#FF00FF', '#00BFFF', '#008000', '#C0C0C0', '#FF0000'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart in Streamlit
        st.pyplot(fig)
if __name__ == "__main__":
    main()
st.caption('Oleh Egi Erlangga')
