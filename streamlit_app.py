import streamlit as st

st.set_page_config(page_title="Limbah Edu", layout="centered")

st.title("🌿 Aplikasi Edukasi Pengolahan Limbah Industri")

# Sidebar Menu
menu = st.sidebar.radio("📚 Menu", ["Beranda", "Materi", "Kalkulator COD", "Upload Laporan", "Kontak"])

# Halaman Beranda
if menu == "Beranda":
    st.subheader("Selamat Datang 👋")
    st.write("""
        Aplikasi ini ditujukan untuk mahasiswa yang mempelajari pengolahan limbah industri.
        Silakan pilih menu di samping untuk memulai.
    """)
    st.image("https://images.unsplash.com/photo-1611080626919-7a7487f1e8e2", use_column_width=True)

# Halaman Materi
elif menu == "Materi":
    st.subheader("📘 Materi Pembelajaran")
    st.markdown("""
    1. **Pengenalan Limbah Industri**  
    2. **Metode Pengolahan Limbah**  
       - Fisika (filtrasi, sedimentasi)  
       - Kimia (netralisasi, koagulasi)  
       - Biologi (aerob, anaerob)  
    3. **Parameter Penting**  
       - pH, TSS, BOD, COD  
    4. **Regulasi Lingkungan**  
       - Standar baku mutu limbah
    """)
    st.info("Materi lengkap bisa diunggah atau ditambahkan di versi selanjutnya.")

# Halaman Kalkulator COD
elif menu == "Kalkulator COD":
    st.subheader("🧪 Kalkulator COD (Chemical Oxygen Demand)")

    st.markdown("### Masukkan Data")
    V = st.number_input("Volume titran (mL)", min_value=0.0, format="%.2f")
    N = st.number_input("Normalitas titran (N)", min_value=0.0, format="%.4f")
    sample_vol = st.number_input("Volume sampel (mL)", min_value=0.0, format="%.2f")

    if st.button("Hitung COD"):
        if sample_vol > 0:
            cod = (V * N * 8000) / sample_vol
            st.success(f"Hasil COD: {cod:.2f} mg/L")
        else:
            st.error("Volume sampel harus lebih dari 0!")

# Halaman Upload Laporan
elif menu == "Upload Laporan":
    st.subheader("📤 Upload Laporan Praktikum")

    uploaded_file = st.file_uploader("Pilih file PDF", type="pdf")
    if uploaded_file is not None:
        st.success(f"Berhasil mengunggah: {uploaded_file.name}")
        st.write("Catatan: File hanya disimpan sementara (belum terhubung ke database).")

# Halaman Kontak
elif menu == "Kontak":
    st.subheader("📞 Kontak Dosen/Admin")
    st.markdown("""
    - 📧 **Email**: limbahedu@kampus.ac.id  
    - 📱 **WhatsApp**: [Klik untuk chat](https://wa.me/6281234567890)
    - 🌐 **Website**: [limbahedu.streamlit.app](https://limbahedu.streamlit.app)
    """)
