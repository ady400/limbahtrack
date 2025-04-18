import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Pengolahan Limbah Industri", layout="wide")

# Sidebar Navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Menu", ["Beranda", "Proses Pengolahan", "Kalkulator Uji COD", "Tentang Aplikasi"])

# Gaya CSS custom
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            color: #2c3e50;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #34495e;
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

# Halaman Beranda
if page == "Beranda":
    st.markdown('<div class="title">Selamat Datang di Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1581091870622-27a0b8c52f5c", caption="Industri & Lingkungan", use_column_width=True)
    st.markdown("""
        Aplikasi ini dirancang untuk membantu pengguna memahami proses pengolahan limbah industri serta melakukan simulasi sederhana uji parameter kimia seperti *Chemical Oxygen Demand (COD)*.
        Navigasikan menu di sebelah kiri untuk menjelajahi fitur yang tersedia.
    """)

# Halaman Proses Pengolahan
elif page == "Proses Pengolahan":
    st.markdown('<div class="title">Proses Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.markdown("""
    Limbah industri memerlukan pengolahan sebelum dibuang ke lingkungan agar tidak mencemari ekosistem. Berikut beberapa tahap utama:
    
    1. *Pre-treatment (Pra-Pengolahan):* Penyaringan kasar, penghilangan padatan besar.
    2. *Pengolahan Primer:* Pemisahan padatan tersuspensi melalui sedimentasi.
    3. *Pengolahan Sekunder:* Proses biologis untuk menguraikan bahan organik.
    4. *Pengolahan Tersier:* Penghilangan zat kimia tersisa dan disinfeksi.
    5. *Pembuangan Aman:* Pembuangan limbah yang sudah diolah ke badan air atau digunakan kembali.

    Gunakan grafik atau diagram untuk memahami lebih lanjut.
    """)
    st.image("https://www.researchgate.net/profile/Asma-Murad/publication/319504162/figure/fig1/AS:699713568567296@1541910371073/Flow-chart-of-industrial-wastewater-treatment-plant.png", caption="Diagram Proses Pengolahan", use_column_width=True)

# Halaman Kalkulator Uji COD
elif page == "Kalkulator Uji COD":
    st.markdown('<div class="title">Kalkulator Uji COD (Chemical Oxygen Demand)</div>', unsafe_allow_html=True)
    st.markdown("Masukkan data uji COD di bawah ini untuk menghitung konsentrasi COD dalam sampel limbah:")

    # Input user
    volume_titran = st.number_input("Volume titran (mL)", min_value=0.0, value=10.0)
    normalitas_titran = st.number_input("Normalitas titran (N)", min_value=0.0, value=0.25)
    volume_sampel = st.number_input("Volume sampel (mL)", min_value=1.0, value=50.0)

    if st.button("Hitung COD"):
        cod_mg_per_l = (volume_titran * normalitas_titran * 8000) / volume_sampel
        st.success(f"Konsentrasi COD: {cod_mg_per_l:.2f} mg/L")

# Halaman Tentang Aplikasi
elif page == "Tentang Aplikasi":
    st.markdown('<div class="title">Tentang Aplikasi</div>', unsafe_allow_html=True)
    st.markdown("""
    Aplikasi ini dikembangkan untuk memberikan edukasi dan alat bantu dalam pemahaman serta pengelolaan limbah industri.

    *Fitur utama:*
    - Informasi proses pengolahan limbah industri
    - Kalkulator uji laboratorium (COD)
    - Antarmuka interaktif dan informatif

    *Dibuat menggunakan:* Python + Streamlit  
    *Pengembang:* [Nama Kamu / Tim Pengembang]  
    *Versi:* 1.0.0  
    """)
