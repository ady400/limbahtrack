import time
import numpy as np
import pandas as pd
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Limbah Industri", layout="wide")

# Navigasi Sidebar
menu = st.sidebar.radio("Menu", ["Beranda", "Proses", "Uji Lab", "Simulasi", "Tentang"])

# BERANDA
if menu == "Beranda":
    st.markdown("""
    <div style='text-align: center; padding: 30px 0;'>
        <h1 style='color:#2C3E50;'>Aplikasi Pengolahan Limbah Industri</h1>
        <p style='font-size:18px; color:#555;'>Belajar dan simulasi proses pengolahan limbah industri secara interaktif dan edukatif</p>
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
elif menu == "Proses":
    st.markdown("<h2 style='color:#2C3E50;'>Tahapan Pengolahan Limbah Industri</h2>", unsafe_allow_html=True)
    st.markdown("Pelajari ringkasan tiap tahap proses secara visual.")

    tahap_list = [
        {
            "judul": "Pra-Pengolahan",
            "ikon": "https://cdn-icons-png.flaticon.com/512/10761/10761283.png",
            "deskripsi": "Pemisahan benda kasar dan partikel berat menggunakan screening, grit chamber, dan equalization tank."
        },
        {
            "judul": "Pengolahan Primer",
            "ikon": "https://cdn-icons-png.flaticon.com/512/2503/2503508.png",
            "deskripsi": "Pengendapan awal untuk menghilangkan padatan tersuspensi dan menghasilkan primary sludge."
        },
        {
            "judul": "Pengolahan Sekunder",
            "ikon": "https://cdn-icons-png.flaticon.com/512/4320/4320337.png",
            "deskripsi": "Pengolahan biologis menggunakan mikroorganisme (aerob dan anaerob) untuk menguraikan bahan organik."
        },
        {
            "judul": "Pengolahan Tersier",
            "ikon": "https://cdn-icons-png.flaticon.com/512/2917/2917991.png",
            "deskripsi": "Menghilangkan kontaminan sisa seperti nutrien dan logam berat melalui filtrasi dan proses kimia."
        },
        {
            "judul": "Pengolahan Lumpur",
            "ikon": "https://cdn-icons-png.flaticon.com/512/9799/9799171.png",
            "deskripsi": "Mengurangi volume dan menstabilkan lumpur melalui thickening, dewatering, dan digestion."
        },
        {
            "judul": "Pembuangan Akhir",
            "ikon": "https://cdn-icons-png.flaticon.com/512/7443/7443442.png",
            "deskripsi": "Air olahan dibuang ke lingkungan atau dimanfaatkan kembali untuk irigasi dan industri."
        }
    ]

    for i in range(0, len(tahap_list), 2):
        col1, col2 = st.columns(2)
        for j, col in enumerate([col1, col2]):
            if i + j < len(tahap_list):
                tahap = tahap_list[i + j]
                with col:
                    st.image(tahap["ikon"], width=50)
                    st.markdown(f"#### {tahap['judul']}")
                    st.write(tahap["deskripsi"])
# KALKULATOR LAB
elif menu == "Uji Lab":
    st.markdown('<div class="main-title">Kalkulator Uji Lab</div>', unsafe_allow_html=True)
    uji = st.selectbox("Pilih jenis uji:", ["COD", "BOD", "TSS", "pH"])

    if uji == "COD":
        v = st.number_input("Volume titran (mL)", value=10.0)
        n = st.number_input("Normalitas titran (N)", value=0.25)
        vs = st.number_input("Volume sampel (mL)", value=50.0)
        if st.button("Hitung"):
            hasil = (v * n * 8000) / vs
            st.success(f"COD = {hasil:.2f} mg/L")

    elif uji == "BOD":
        awal = st.number_input("DO Awal (mg/L)", value=8.0)
        akhir = st.number_input("DO Akhir (mg/L)", value=2.0)
        if st.button("Hitung"):
            hasil = awal - akhir
            st.success(f"BOD = {hasil:.2f} mg/L")

    elif uji == "TSS":
        awal = st.number_input("Berat filter awal (mg)", value=100.0)
        akhir = st.number_input("Berat filter akhir (mg)", value=120.0)
        volume = st.number_input("Volume sampel (L)", value=1.0)
        if st.button("Hitung"):
            hasil = (akhir - awal) / volume
            st.success(f"TSS = {hasil:.2f} mg/L")

    elif uji == "pH":
        ph = st.slider("pH sampel", 0.0, 14.0, 7.0)
        st.info(f"pH = {ph}")

# SIMULASI
elif menu == "Simulasi":
    st.markdown('<div class="main-title">Simulasi Pengolahan</div>', unsafe_allow_html=True)
    jenis = st.selectbox("Jenis limbah", ["Organik", "Kimia", "Campuran"])
    awal = st.number_input("Konsentrasi awal (mg/L)", value=500.0)

    efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]
    if st.button("Simulasi"):
        akhir = awal * (1 - efisiensi)
        st.success(f"Hasil akhir: {akhir:.2f} mg/L ({efisiensi*100:.0f}% efisiensi)")

# TENTANG
elif menu == "Tentang":
    st.markdown('<div class="main-title">Tentang Aplikasi</div>', unsafe_allow_html=True)
    st.write("""
    Aplikasi edukatif ini dibuat untuk mengenalkan proses pengolahan limbah industri secara interaktif.

    - Teknologi: Python + Streamlit  
    - Pengembang: Kelompok 6 1F PLI AKA  
    - Versi: 1.0  
    - Sumber: Modul Teknik Lingkungan, Litbang KLHK
    """)
