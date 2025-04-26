import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Limbah Industri", layout="wide")

# Navigasi Sidebar
menu = st.sidebar.radio("Menu", ["Beranda", "Proses", "Uji Lab", "Simulasi", "Tentang"])

# Styling sederhana
st.markdown("""
    <style>
        .main-title { font-size: 30px; color: #2c3e50; font-weight: bold; }
        .section-title { font-size: 22px; color: #34495e; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# BERANDA
if menu == "Beranda":
    st.markdown('<div class="main-title">Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.write("Aplikasi ini dirancang untuk membantu memahami dan mensimulasikan pengolahan limbah industri secara sederhana dan interaktif.")

# PROSES
elif menu == "Proses":
    st.markdown('<div class="main-title">Tahapan Pengolahan Limbah</div>', unsafe_allow_html=True)

    st.markdown("## 1. Pra-pengolahan")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bar_Screen.png/640px-Bar_Screen.png", caption="Contoh bar screen untuk menyaring partikel kasar")
    st.markdown("""
    Tahap ini bertujuan untuk menyaring partikel besar seperti plastik, kayu, dan pasir dari air limbah.
    Alat yang digunakan: *bar screen, **grit chamber*.
    """)

    st.markdown("## 2. Pengolahan Primer")
    st.image("https://www.researchgate.net/profile/Azam-Rashidi/publication/317398778/figure/fig1/AS:613808246849546@1523377437292/Schematic-of-primary-treatment-process-of-wastewater.png", caption="Skema pengendapan primer")
    st.markdown("""
    Limbah dialirkan ke tangki pengendapan untuk memisahkan partikel tersuspensi secara gravitasi.
    Hasil: air limbah lebih jernih & lumpur primer.
    """)

    st.markdown("## 3. Pengolahan Sekunder")
    st.image("https://www.epa.ie/media/epa/images/secondary-treatment.jpg", caption="Proses biologis dengan mikroorganisme")
    st.markdown("""
    Menggunakan mikroorganisme aerob atau anaerob untuk menguraikan bahan organik.
    Sistem umum: *lumpur aktif, **kolam oksidasi, **biofilter*.
    """)

    st.markdown("## 4. Pengolahan Tersier")
    st.image("https://www.researchgate.net/publication/327157481/figure/fig3/AS:666554944987141@1536104400082/Tertiary-Treatment-of-Wastewater.png", caption="Disinfeksi dan penghilangan nutrien")
    st.markdown("""
    Menghilangkan polutan lanjutan seperti fosfat, nitrat, logam berat, dan mikroorganisme patogen.
    Teknologi: *ozonisasi, **UV, **filtrasi pasir, **reverse osmosis*.
    """)

    st.markdown("## 5. Pembuangan Akhir")
    st.image("https://www.aqua-calc.com/images/discharge.png", caption="Pembuangan ke badan air")
    st.markdown("""
    Air limbah yang telah memenuhi standar baku mutu dibuang ke sungai, laut, atau dimanfaatkan kembali (reuse).
    Lumpur sisa diolah dengan pengeringan atau pembakaran.
    """)

    st.markdown("---")
    st.markdown("## Video Edukasi Pendek")

    st.video("https://www.youtube.com/watch?v=U1c_XK1uK5I")
    st.caption("Animasi proses pengolahan limbah yang sederhana dan mudah dipahami.")

    st.video("https://www.youtube.com/watch?v=Wffd9BynYO0")
    st.caption("Simulasi 3D sistem pengolahan air limbah secara komprehensif.")

    st.success("Dengan memahami tahapan ini, kita dapat menjaga lingkungan dari pencemaran limbah secara lebih efektif.")
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

    - *Teknologi:* Python + Streamlit  
    - *Pengembang:* [Nama Anda]  
    - *Versi:* 1.0  
    - *Sumber:* Modul Teknik Lingkungan, Litbang KLHK
    """)
