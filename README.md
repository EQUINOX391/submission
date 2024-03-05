# Data Analysis With Python : E-Commerce Olist Brazil

## Konten
Repositori ini berisi tentang proses analisis dataset ecommerce olist brazil menggunakan python dan divisualisasikan secara komprehensif dengan streamlit
- Kategori produk populer dan tidak populer tiap bulan
- Total belanja pelanggan tiap bulan
- Total pemesanan barang tiap bulan
- Pengeluaran vs pemesanan tiap bulan
- Produk teratas tiap bulan
- Pelanggan tiap negara bagian
- Pelanggan tiap kota
- Persebaran pelanggan dalam peta negara brazil
- Recency
- Frequency
- Monetary
- 3D RFM analysis
- Segmentasi pelanggan berdasarkan perilaku
- Segmentasi pelanggan berdasarkan skor ranking

## Requirements
Semua kebutuhan untuk project ini sebenarnya sudah aku masukkan ke dalam file "Requirements.txt", kamu tinggal jalankan perintah
> pip install -r Requirements.txt

setelah itu kamu akan melihat seluruh librari yang dibutuhkan sudah terinstal dan kamu siap menggunakan repositori ini

> [!TIP]
Jika kamu mau mendownload datasetnya via API kaggle, kamu bisa uncomment bagian Importing Dataset, dan ikuti [tutorial ini](https://www.kaggle.com/discussions/general/74235)

## Setup Environments
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run Streamlit App
```
streamlit run dashboard.py
```

## Sumber Dataset
Brazilian E-Commerce Public Dataset by Olist 
>(https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
