import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Limbah Industri", layout="wide")

# Navigasi Sidebar
menu = st.sidebar.radio("Menu", ["Beranda", "Proses", "Uji Lab", "Simulasi", "Tentang"])

# Background image styling
st.markdown("""
    <style>
        body{
            background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fliberty-society.com%2Fid%2Fblogs%2Fblog-1%2Fdaur-ulang-sampah-kertas&psig=AOvVaw3IknIiqzLjstZEFSm1Vrv8&ust=1745718968002000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPiLsLjM9IwDFQAAAAAdAAAAABAE')
            background-position: center;
            background-size: cover;
            text-aligin: center;
            height: 100vh;
            padding: 100px;
        }
        
    </style>
""", unsafe_allow_html=True)

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
    st.image
    st.write("Aplikasi ini dirancang untuk membantu memahami dan mensimulasikan pengolahan limbah industri secara sederhana dan interaktif.")

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

    - *Teknologi:* Python + Streamlit  
    - *Pengembang:* [Nama Anda]  
    - *Versi:* 1.0  
    - *Sumber:* Modul Teknik Lingkungan, Litbang KLHK
    """)
