import time
import numpy as np
import pandas as pd
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Limbah Industri", page_icon="♻️", layout="wide")

# Sidebar
with st.sidebar:
    st.image("https://pixabay.com/id/vectors/daur-ulang-mendaur-ulang-kaca-44111/", width=1000)
    st.title("♻️ Limbah Industri")
    st.markdown("**Belajar & Simulasi Pengolahan Limbah Industri** 🌍")
    st.markdown("---")
    menu = st.radio("Navigasi", ["🏠 Beranda", "⚙️ Proses", "🧪 Uji Lab", "🧩 Simulasi", "ℹ️ Tentang"])
    st.markdown("---")
    st.caption("© 2025 Kelompok 6 - 1F PLI AKA")

# CSS tambahan buat mempercantik
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        color: #2C3E50;
        text-align: center;
        padding: 20px 0;
    }
    .stButton>button {
        background-color: #2C3E50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# BERANDA
if menu == "🏠 Beranda":
    st.markdown("""
    <div style='text-align: center; padding: 30px 0;'>
        <h1 style='color:#2C3E50;'>♻️ Aplikasi Pengolahan Limbah Industri ♻️</h1>
        <p style='font-size:18px; color:#555;'>Belajar dan simulasi proses pengolahan limbah industri secara interaktif dan edukatif.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/1866/1866365.png", width=80)
        st.markdown("### Edukasi Proses")
        st.write("Kenali tahapan pengolahan limbah dari awal hingga akhir.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135823.png", width=80)
        st.markdown("### Uji Laboratorium")
        st.write("Hitung nilai COD, BOD, TSS, dan pH dari data sampel.")
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2933/2933820.png", width=80)
        st.markdown("### Simulasi Interaktif")
        st.write("Lakukan simulasi pengolahan limbah dengan berbagai jenis.")

# PROSES
elif menu == "⚙️ Proses":
    st.markdown('<div class="main-title">⚙️ Tahapan Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 🧹 1. Pra-Pengolahan (Pre-Treatment)
    - *Screening:* Menyaring benda kasar seperti plastik dan kayu.
    - *Grit Chamber:* Mengendapkan partikel berat seperti pasir.
    - *Equalization Tank:* Menyeimbangkan aliran dan beban limbah.

    ### 🧪 2. Pengolahan Primer
    - *Primary Clarifier:* Mengendapkan padatan tersuspensi.

    ### 🧬 3. Pengolahan Sekunder (Biologis)
    - *Aerob:* Dengan oksigen (activated sludge, trickling filter).
    - *Anaerob:* Tanpa oksigen untuk limbah berat.

    ### 🧼 4. Pengolahan Tersier
    - *Filtrasi, Reverse Osmosis, Proses Kimia.*

    ### 🧱 5. Pengolahan Lumpur
    - *Thickening, Digestion, Dewatering.*

    ### 🌊 6. Pembuangan Akhir
    - Limbah cair buangan yang memenuhi standar.
    """)

# UJI LAB
elif menu == "🧪 Uji Lab":
    st.markdown('<div class="main-title">🧪 Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True)
    uji = st.selectbox("Pilih jenis uji:", ["COD", "BOD", "TSS", "pH"])

    if uji == "COD":
        v = st.number_input("Volume titran (mL)", value=10.0)
        n = st.number_input("Normalitas titran (N)", value=0.25)
        vs = st.number_input("Volume sampel (mL)", value=50.0)
        if st.button("Hitung COD"):
            hasil = (v * n * 8000) / vs
            st.success(f"COD = {hasil:.2f} mg/L")

    elif uji == "BOD":
        awal = st.number_input("DO Awal (mg/L)", value=8.0)
        akhir = st.number_input("DO Akhir (mg/L)", value=2.0)
        if st.button("Hitung BOD"):
            hasil = awal - akhir
            st.success(f"BOD = {hasil:.2f} mg/L")

    elif uji == "TSS":
        awal = st.number_input("Berat filter awal (mg)", value=100.0)
        akhir = st.number_input("Berat filter akhir (mg)", value=120.0)
        volume = st.number_input("Volume sampel (L)", value=1.0)
        if st.button("Hitung TSS"):
            hasil = (akhir - awal) / volume
            st.success(f"TSS = {hasil:.2f} mg/L")

    elif uji == "pH":
        ph = st.slider("pH sampel", 0.0, 14.0, 7.0)
        st.info(f"pH = {ph}")

# SIMULASI
elif menu == "🧩 Simulasi":
    st.markdown('<div class="main-title">🔄 Simulasi Pengolahan Limbah</div>', unsafe_allow_html=True)
    jenis = st.selectbox("Jenis limbah", ["Organik", "Kimia", "Campuran"])
    awal = st.number_input("Konsentrasi awal (mg/L)", value=500.0)

    efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]
    if st.button("Mulai Simulasi"):
        akhir = awal * (1 - efisiensi)
        st.success(f"Hasil akhir: {akhir:.2f} mg/L ({efisiensi*100:.0f}% efisiensi)")

# TENTANG
elif menu == "ℹ️ Tentang":
    st.markdown('<div class="main-title">ℹ️ Tentang Aplikasi Ini</div>', unsafe_allow_html=True)
    st.write("""
    Aplikasi edukatif ini dibuat untuk mengenalkan proses pengolahan limbah industri secara interaktif.
    
    - **Teknologi:** Python + Streamlit
    - **Pengembang:** Kelompok 6 - 1F PLI AKA
    - **Versi:** 1.0
    - **Sumber:** Modul Teknik Lingkungan, Litbang KLHK
    """)
                
