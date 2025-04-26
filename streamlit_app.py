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
    <style>
        .main-card {
            background-color: #e0f7fa;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .parameter-box {
            display: flex;
            justify-content: space-around;
            margin-top: 30px;
        }
        .param {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            width: 22%;
            box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .param h3 {
            margin: 10px 0 5px;
        }
        .quick-links a {
            display: inline-block;
            margin-right: 15px;
            padding: 10px 15px;
            background: #00796b;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>

    <div class="main-card">
        <h1>Selamat Datang di Aplikasi Pengolahan Limbah Industri</h1>
        <p>Aplikasi edukatif interaktif untuk memahami proses pengolahan limbah industri dan melakukan simulasi serta pengujian parameter BOD, COD, pH, dan TSS.</p>

        <div class="parameter-box">
            <div class="param">
                <h3>BOD</h3>
                <p>Biological Oxygen Demand</p>
            </div>
            <div class="param">
                <h3>COD</h3>
                <p>Chemical Oxygen Demand</p>
            </div>
            <div class="param">
                <h3>pH</h3>
                <p>Tingkat keasaman</p>
            </div>
            <div class="param">
                <h3>TSS</h3>
                <p>Total Suspended Solids</p>
            </div>
        </div>

        <div style="margin-top: 30px;">
            <h4>Mulai Jelajahi:</h4>
            <div class="quick-links">
                <a href="#Proses">Proses</a>
                <a href="#Uji Lab">Uji Lab</a>
                <a href="#Simulasi">Simulasi</a>
                <a href="#Tentang">Tentang</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
# PROSES
elif menu == "Proses":
    st.markdown("""
<div class="section-title">1. Pra-Pengolahan (Pre-Treatment)</div>
<p>Pada tahap ini, limbah disaring untuk menghilangkan benda padat besar seperti plastik, kayu, atau pasir. Peralatan yang digunakan antara lain:</p>
<ul>
  <li><b>Screening:</b> Menyaring benda kasar</li>
  <li><b>Grit Chamber:</b> Mengendapkan partikel berat seperti pasir</li>
  <li><b>Equalization Tank:</b> Menyeimbangkan aliran dan beban limbah</li>
</ul>

<div class="section-title">2. Pengolahan Primer</div>
<p>Bertujuan menghilangkan padatan tersuspensi dengan cara pengendapan. Lumpur hasil endapan dikumpulkan sebagai <b>primary sludge</b>.</p>
<ul>
  <li><b>Primary Clarifier:</b> Tangki pengendapan yang memisahkan lumpur dari cairan limbah</li>
</ul>

<div class="section-title">3. Pengolahan Sekunder (Biologis)</div>
<p>Proses biologis untuk menguraikan bahan organik menggunakan mikroorganisme.</p>
<ul>
  <li><b>Proses Aerob:</b> Menggunakan oksigen (misalnya activated sludge, trickling filter)</li>
  <li><b>Proses Anaerob:</b> Tanpa oksigen, sering digunakan untuk lumpur atau limbah berkonsentrasi tinggi</li>
</ul>

<div class="section-title">4. Pengolahan Tersier (Lanjutan)</div>
<p>Menghilangkan kontaminan yang tersisa, seperti nutrien, logam berat, atau bahan kimia.</p>
<ul>
  <li>Filtrasi Pasir, Karbon Aktif</li>
  <li>Reverse Osmosis (RO)</li>
  <li>Proses Kimia: Koagulasi, flokulasi, dan disinfeksi (klorinasi, UV)</li>
</ul>

<div class="section-title">5. Pengolahan Lumpur (Sludge Treatment)</div>
<p>Lumpur dari tahap primer dan sekunder perlu diolah sebelum dibuang atau dimanfaatkan.</p>
<ul>
  <li>Thickening, Dewatering</li>
  <li>Digestion: Proses biologis untuk mengurangi volume dan stabilisasi</li>
  <li>Pengeringan dan Pembakaran (jika perlu)</li>
</ul>

<div class="section-title">6. Pembuangan Akhir</div>
<p>Air hasil olahan yang telah memenuhi baku mutu dibuang ke badan air seperti sungai atau laut, atau digunakan kembali (reuse) untuk keperluan industri atau pertanian.</p>
""", unsafe_allow_html=True)
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
