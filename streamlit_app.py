# app.py
import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Limbah Edukasi", layout="wide")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .title-main {
            font-size: 36px;
            font-weight: bold;
            color: #00aa55;
        }
        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 30px;
        }
        .highlight-box {
            background-color: #e0ffe5;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title-main'>🌿 Aplikasi Edukasi Pengolahan Limbah Industri</div>", unsafe_allow_html=True)
st.markdown("Belajar pengolahan limbah industri jadi lebih mudah dan menyenangkan.")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigasi", ["Beranda", "Materi Pembelajaran", "Kalkulator COD/BOD", "Simulasi Proses", "Kuis", "Galeri"])

# --- Beranda ---
if menu == "Beranda":
    st.image("https://images.unsplash.com/photo-1603575448366-a0c47cd45e0f", use_column_width=True)
    st.markdown("""
    <div class="highlight-box">
    ✅ Aplikasi ini dirancang untuk mahasiswa Teknik Lingkungan dan siapa pun yang ingin belajar tentang pengolahan limbah industri.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Tips Menggunakan Aplikasi:")
    st.markdown("- Gunakan sidebar untuk menjelajahi fitur.")
    st.markdown("- Kalkulator COD/BOD bisa bantu hitung parameter laboratorium.")
    st.markdown("- Simulasi cocok untuk visualisasi alur pengolahan limbah.")

# --- Materi Pembelajaran ---
elif menu == "Materi Pembelajaran":
    st.header("📘 Materi Pembelajaran")
    with st.expander("Pengertian Limbah Industri"):
        st.write("Limbah industri adalah limbah yang dihasilkan dari aktivitas industri...")
    with st.expander("Jenis-jenis Limbah"):
        st.write("- Limbah cair\n- Limbah padat\n- Limbah gas")
    with st.expander("Dampak Limbah"):
        st.write("Pencemaran lingkungan, dampak kesehatan, dll.")

# --- Kalkulator COD/BOD ---
elif menu == "Kalkulator COD/BOD":
    st.header("🧪 Kalkulator COD & BOD")
    vol = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.2f")
    normalitas = st.number_input("Normalitas Titrasi (N)", min_value=0.0, format="%.3f")
    titran_blanko = st.number_input("Volume Titrasi Blanko (mL)", min_value=0.0)
    titran_sampel = st.number_input("Volume Titrasi Sampel (mL)", min_value=0.0)
    
    if st.button("Hitung COD"):
        try:
            cod = (titran_blanko - titran_sampel) * normalitas * 8000 / vol
            st.success(f"Hasil COD: {cod:.2f} mg/L")
        except:
            st.error("Input tidak valid.")

# --- Simulasi Proses ---
elif menu == "Simulasi Proses":
    st.header("🧯 Simulasi Proses Pengolahan Limbah")
    proses = st.selectbox("Pilih Tahapan Proses", ["Screening", "Sedimentasi", "Aerasi", "Disinfeksi"])
    if proses == "Screening":
        st.image("https://i.imgur.com/Yz9D1tP.png")
        st.write("Screening bertujuan menyaring benda besar seperti plastik...")
    elif proses == "Sedimentasi":
        st.image("https://i.imgur.com/oQKq8N3.png")
        st.write("Proses ini memisahkan partikel padat dari cairan...")
    elif proses == "Aerasi":
        st.image("https://i.imgur.com/C8jqF1g.png")
        st.write("Aerasi menambah oksigen terlarut untuk mendukung bakteri pengurai...")
    else:
        st.image("https://i.imgur.com/xVu6Ypi.png")
        st.write("Disinfeksi menggunakan klorin atau ozon untuk membunuh mikroorganisme...")

# --- Kuis Interaktif ---
elif menu == "Kuis":
    st.header("📝 Kuis Pengolahan Limbah")
    q1 = st.radio("1. Apa tujuan dari proses aerasi?", ["Menyari…
