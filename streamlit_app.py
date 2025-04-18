import streamlit as st

# Konfigurasi
st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

# Sidebar Navigasi
menu = st.sidebar.selectbox("Navigasi", ["Beranda", "Proses Pengolahan", "Kalkulator Uji Lab", "Simulasi Pengolahan", "Tentang Aplikasi"])

# CSS untuk styling
st.markdown("""
    <style>
        .title { font-size: 36px; color: #2c3e50; font-weight: bold; }
        .subtitle { font-size: 24px; color: #34495e; } 
        </style>""", unsafe_allow_html=True)

# Halaman: Beranda
if menu == "Beranda":
    st.markdown('<div class="title">Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Edukasi | Simulasi | Lingkungan</div>', unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.image(https://pin.it/eRwr0NH6O, use_column_width=True)
    with col2:
        st.write("""
        Selamat datang di aplikasi *Pengolahan Limbah Industri*, sebuah platform interaktif yang dirancang untuk:
        - Memberikan edukasi tentang proses pengolahan limbah
        - Menyediakan alat bantu simulasi pengujian kualitas air limbah
        - Menumbuhkan kesadaran terhadap pentingnya pengelolaan limbah yang berkelanjutan

        *Mengapa ini penting?*  
        Karena pengolahan limbah yang buruk bisa mencemari air, tanah, dan merusak ekosistem.
        """)

    st.write("### Fitur Unggulan")
    fitur = {
        "⚙️ Proses Pengolahan": "Pelajari tahapan penting dalam pengolahan limbah industri.",
        "🧪 Kalkulator Lab": "Simulasikan uji COD, BOD, pH, dan TSS dengan mudah.",
        "📊 Simulasi Pengolahan": "Uji efisiensi sistem pengolahan berdasarkan jenis limbah.",
        "ℹ️ Tentang Aplikasi": "Kenali aplikasi dan pengembang di baliknya."
    }

    for icon, desc in fitur.items():
        st.markdown(f"*{icon}* – {desc}")
# Halaman: Proses Pengolahan
elif menu == "Proses Pengolahan":
    st.markdown('<div class="title">Proses Pengolahan Limbah</div>', unsafe_allow_html=True)
    st.markdown("""
    Berikut tahapan umum pengolahan limbah:
    
    1. *Pra-pengolahan:* Penyaringan kasar, pemisahan padatan besar.  
    2. *Pengolahan Primer:* Sedimentasi untuk mengendapkan partikel.  
    3. *Pengolahan Sekunder:* Proses biologis (aerob/anaerob).  
    4. *Pengolahan Tersier:* Penghilangan senyawa kimia & disinfeksi.  
    5. *Pembuangan Aman:* Air hasil olahan dibuang sesuai standar baku mutu.
    """)

# Halaman: Kalkulator Uji Lab
elif menu == "Kalkulator Uji Lab":
    st.markdown('<div class="title">Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True)
    opsi = st.radio("Pilih Uji:", ["COD", "BOD", "TSS", "pH"])

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
        berat_filter_awal = st.number_input("Berat filter awal (mg)", 0.0, 1000.0, 100.0)
        berat_filter_akhir = st.number_input("Berat filter akhir (mg)", 0.0, 1000.0, 120.0)
        volume_air = st.number_input("Volume sampel (L)", 0.1, 10.0, 1.0)
        if st.button("Hitung TSS"):
            TSS = (berat_filter_akhir - berat_filter_awal) / volume_air
            st.success(f"Hasil TSS: {TSS:.2f} mg/L")

    elif opsi == "pH":
        ph_val = st.slider("Masukkan nilai pH", 0.0, 14.0, 7.0)
        st.info(f"Nilai pH sampel adalah {ph_val}")

# Halaman: Simulasi Pengolahan
elif menu == "Simulasi Pengolahan":
    st.markdown('<div class="title">Simulasi Efisiensi Pengolahan</div>', unsafe_allow_html=True)
    jenis_limbah = st.selectbox("Jenis Limbah", ["Organik", "Kimia", "Campuran"])
    konsentrasi_awal = st.number_input("Konsentrasi Awal (mg/L)", 0.0, 10000.0, 500.0)
    efisiensi = 0

    if jenis_limbah == "Organik":
        efisiensi = 0.85
    elif jenis_limbah == "Kimia":
        efisiensi = 0.70
    elif jenis_limbah == "Campuran":
        efisiensi = 0.60

    if st.button("Simulasikan"):
        hasil = konsentrasi_awal * (1 - efisiensi)
        st.success(f"Hasil akhir setelah pengolahan: {hasil:.2f} mg/L (efisiensi {efisiensi*100:.0f}%)")
