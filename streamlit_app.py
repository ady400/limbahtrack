import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

# CSS kustom
st.markdown("""
    <style>
    /* Add custom CSS here */
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigasi dengan ikon (opsional)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1076/1076742.png", width=60)
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Beranda", "Proses Pengolahan", "Kalkulator Uji Lab", "Simulasi Pengolahan", "Tentang Aplikasi"])

# BERANDA
if menu == "Beranda":
    st.markdown('**Selamat Datang di Aplikasi Pengolahan Limbah Industri**', unsafe_allow_html=True)
    st.markdown('Simulasi Menuju Lingkungan Bersih dan Berkelanjutan', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Gambar Dicoding yang benar
        st.image("https://www.dicoding.com/assets/img/brand/dicoding-logo.svg", use_column_width=True)
    with col2:
        st.success("""
            Aplikasi ini dirancang sebagai alat bantu edukatif:
            - Menjelaskan **tahapan pengolahan limbah industri**
            - Memberikan **simulasi pengujian COD, BOD, pH, dan TSS**
            - Meningkatkan kesadaran akan pentingnya pengelolaan limbah
        """)

# PROSES PENGOLAHAN
elif menu == "Proses Pengolahan":
    st.markdown('**Tahapan Pengolahan Limbah**', unsafe_allow_html=True)
    st.info("Berikut ini adalah tahapan umum dalam pengolahan limbah industri:")
    st.markdown("""
    1. **Pra-pengolahan**: Penyaringan kasar, pemisahan padatan besar
    2. **Pengolahan Primer**: Sedimentasi untuk mengendapkan partikel
    3. **Pengolahan Sekunder**: Proses biologis (aerob/anaerob)
    4. **Pengolahan Tersier**: Penghilangan senyawa kimia & disinfeksi
    5. **Pembuangan Aman**: Air hasil olahan dibuang sesuai standar baku mutu
    """)

# Kalkulator, Simulasi, dan Tentang Aplikasi tetap sama seperti yang sebelumnya.
