import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set title and layout
st.set_page_config(page_title="Pengolahan Limbah Industri", layout="wide")
st.title("Pengolahan Limbah Industri")
st.markdown("<style>body{background-color: #e0f7e0;}</style>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigasi")
options = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Statistik", "Berita Terbaru"])

# Beranda
if options == "Beranda":
    st.header("Selamat Datang di Aplikasi Pengolahan Limbah Industri")
    st.write("Aplikasi ini bertujuan untuk memberikan informasi dan statistik mengenai pengolahan limbah industri.")
    st.image("https://example.com/image.jpg", caption="Pengolahan Limbah Industri", use_column_width=True)

# Statistik
elif options == "Statistik":
    st.header("Statistik Pengolahan Limbah")
    # Contoh data
    data = {
        'Jenis Limbah': ['Limbah Cair', 'Limbah Padat', 'Limbah Gas'],
        'Jumlah (ton)': [1500, 800, 300]
    }
    df = pd.DataFrame(data)

    # Tampilkan tabel
    st.write("Tabel Statistik:")
    st.dataframe(df)

    # Grafik
    st.bar_chart(df.set_index('Jenis Limbah'))

# Berita Terbaru
elif options == "Berita Terbaru":
    st.header("Berita Terbaru tentang Pengolahan Limbah")
    st.write("1. Inovasi dalam Pengolahan Limbah Cair di Indonesia.")
    st.write("2. Peraturan Baru tentang Pengelolaan Limbah Padat.")
    st.write("3. Teknologi Terbaru dalam Pengurangan Limbah Gas.")

# Footer
st.markdown("---")
st.write("Aplikasi ini dibuat untuk meningkatkan kesadaran tentang pentingnya pengolahan limbah industri.")
