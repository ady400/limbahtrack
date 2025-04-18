import streamlit as st 

Konfigurasi halaman

st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

CSS kustom

st.markdown(""" <style> .title { font-size: 36px; color: #1b5e20; font-weight: bold; text-align: center; margin-bottom: 20px; } .subtitle { font-size: 20px; color: #388e3c; text-align: center; margin-bottom: 40px; } .sidebar .sidebar-content { background-color: #e8f5e9; padding: 20px; } </style> """, unsafe_allow_html=True)

Sidebar Navigasi dengan ikon (opsional)

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1076/1076742.png", width=60) st.sidebar.title("Navigasi") menu = st.sidebar.radio("Pilih Halaman", [ "Beranda", "Proses Pengolahan", "Kalkulator Uji Lab", "Simulasi Pengolahan", "Tentang Aplikasi" ])

BERANDA

if menu == "Beranda": st.markdown('<div class="title">Selamat Datang di Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True) st.markdown('<div class="subtitle">Simulasi Menuju Lingkungan Bersih dan Berkelanjutan</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1600691962274-d2f71c82b9cd", use_column_width=True)
with col2:
    st.success("""
    Aplikasi ini dirancang sebagai alat bantu edukatif:
    - Menjelaskan *tahapan pengolahan limbah industri*
    - Memberikan *simulasi pengujian COD, BOD, pH, dan TSS*
    - Meningkatkan kesadaran akan pentingnya pengelolaan limbah
    """)

PROSES PENGOLAHAN

elif menu == "Proses Pengolahan": st.markdown('<div class="title">Tahapan Pengolahan Limbah</div>', unsafe_allow_html=True) st.info("Berikut ini adalah tahapan umum dalam pengolahan limbah industri:") st.markdown(""" 1. Pra-pengolahan: Penyaringan kasar, pemisahan padatan besar
2. Pengolahan Primer: Sedimentasi untuk mengendapkan partikel
3. Pengolahan Sekunder: Proses biologis (aerob/anaerob)
4. Pengolahan Tersier: Penghilangan senyawa kimia & disinfeksi
5. Pembuangan Aman: Air hasil olahan dibuang sesuai standar baku mutu """)

KALKULATOR UJI LAB

elif menu == "Kalkulator Uji Lab": st.markdown('<div class="title">Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True) opsi = st.radio("Pilih Uji:", ["COD", "BOD", "TSS", "pH"])

if opsi == "COD":
    V = st.number_input("Volume titran (mL)", 0.0, 100.0, 10.0)
    N = st.number_input("Normalitas titran (N)", 0.0, 1.0, 0.25)
    V_sampel = st.number_input("Volume sampel (mL)", 1.0, 1000.0, 50.0)
    if st.button("Hitung COD"):
        COD = (V * N * 8000) / V_sampel
        st.success(f"Hasil COD: {COD:.2f} mg/L")

elif opsi == "BOD":
    DO_awal = st.number_input("DO Awal (mg/L)", 0.0, 20.0, 8.0)
    DO_akhir = st.number_input("DO Akhir (mg/L)", 0.0, 20.0, 2.0)
    if st.button("Hitung BOD"):
        BOD = DO_awal - DO_akhir
        st.success(f"Hasil BOD: {BOD:.2f} mg/L")

elif opsi == "TSS":
    awal = st.number_input("Berat filter awal (mg)", 0.0, 1000.0, 100.0)
    akhir = st.number_input("Berat filter akhir (mg)", 0.0, 1000.0, 120.0)
    volume = st.number_input("Volume sampel (L)", 0.1, 10.0, 1.0)
    if st.button("Hitung TSS"):
        TSS = (akhir - awal) / volume
        st.success(f"Hasil TSS: {TSS:.2f} mg/L")

elif opsi == "pH":
    ph_val = st.slider("Masukkan nilai pH", 0.0, 14.0, 7.0)
    st.info(f"Nilai pH sampel adalah {ph_val}")

SIMULASI PENGOLAHAN

elif menu == "Simulasi Pengolahan": st.markdown('<div class="title">Simulasi Efisiensi Pengolahan Limbah</div>', unsafe_allow_html=True) jenis = st.selectbox("Jenis Limbah", ["Organik", "Kimia", "Campuran"]) kons_awal = st.number_input("Konsentrasi Awal (mg/L)", 0.0, 10000.0, 500.0)

efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]

if st.button("Simulasikan"):
    hasil = kons_awal * (1 - efisiensi)
    st.success(f"Konsentrasi akhir: {hasil:.2f} mg/L | Efisiensi {efisiensi*100:.0f}%")

TENTANG APLIKASI

elif menu == "Tentang Aplikasi": st.markdown('<div class="title">Tentang Aplikasi</div>', unsafe_allow_html=True) st.write(""" Aplikasi Edukasi dan Simulasi Limbah Industri

- Dibuat dengan: Python + Streamlit  
- Tema: Hijau (Eco-Friendly) & Daur Ulang  
- Developer: [Nama Kamu]  
- Versi: 1.0  
- Tujuan: Meningkatkan pemahaman & kesadaran lingkungan
""")
