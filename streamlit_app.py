import streamlit as st
import pandas as pd
# Sidebar Menu
menu = st.sidebar.radio("📚 Pilih Halaman", ["Beranda", "Materi", "Kalkulator COD", "Upload Laporan", "Kontak"])

# ---------- Halaman BERANDA ----------
if menu == "Beranda":
   if menu == "Beranda":
    st.set_page_config(page_title="Aplikasi Edukasi Limbah Industri", layout="wide")

# Header
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #2E7D32;'>🌿 Selamat Datang di Aplikasi Edukasi Limbah Industri</h1>
        <p style='font-size: 18px;'>Belajar pengolahan limbah industri jadi lebih mudah dan menyenangkan.</p>
    </div>
""", unsafe_allow_html=True)

# Gambar Utama
st.image("https://cdn-icons-png.flaticon.com/512/3815/3815447.png", width=150)

# Info Box
with st.container():
    st.success("✅ Aplikasi ini dirancang untuk mahasiswa Teknik Lingkungan dan sejenisnya.")

# Tips Section
st.markdown("### 📌 Tips Menggunakan Aplikasi Ini:")
st.markdown("""
- Navigasikan materi melalui sidebar ⬅️  
- Gunakan *Kalkulator COD* untuk bantu hitung parameter laboratorium  
- Ikuti urutan pembelajaran secara bertahap
""")

# Optional: Tambah menu lainnya atau link ke halaman lain
st.markdown("---")
st.markdown("© 2025 EduWaste App | Dibuat untuk pembelajaran")

# ---------- Halaman MATERI ----------
if materi== "materi":
    st.subheader("📘 Materi Pembelajaran")#<-terlalu banyak spasi
    st.info("Klik untuk membuka tiap topik 👇")

    with st.expander("📖 Pengenalan Limbah Industri"):
        st.write("""
        Limbah industri adalah sisa hasil kegiatan industri, baik berupa cair, padat, maupun gas.
        Pengelolaan yang baik sangat penting untuk mencegah pencemaran lingkungan.
        """)

    with st.expander("🔬 Metode Pengolahan Limbah"):
        st.write("""
        Terdiri dari beberapa jenis:
        - **Fisika**: Sedimentasi, filtrasi
        - **Kimia**: Netralisasi, koagulasi
        - **Biologi**: Pengolahan aerob dan anaerob
        """)

    with st.expander("📊 Parameter Penting"):
        st.write("Beberapa parameter kualitas air limbah:")
        st.markdown("- pH\n- TSS (Total Suspended Solid)\n- BOD\n- COD")

# ---------- Halaman KALKULATOR COD ----------
elif menu == "Kalkulator COD":
    st.subheader("🧪 Kalkulator COD (Chemical Oxygen Demand)")
    st.write("Gunakan rumus: ")
    st.latex(r'COD = \frac{(V \times N \times 8000)}{Volume\ Sampel}')

    V = st.number_input("🔹 Volume titran (mL)", min_value=0.0, format="%.2f")
    N = st.number_input("🔹 Normalitas titran (N)", min_value=0.0, format="%.4f")
    sample_vol = st.number_input("🔹 Volume sampel (mL)", min_value=0.0, format="%.2f")

    if st.button("Hitung COD"):
        if sample_vol > 0:
            cod = (V * N * 8000) / sample_vol
            st.success(f"✅ Hasil COD: {cod:.2f} mg/L")
        else:
            st.error("❌ Volume sampel harus lebih dari 0!")

# ---------- Halaman UPLOAD ----------
elif menu == "Upload Laporan":
    st.subheader("📤 Upload Laporan Praktikum")
    st.markdown("Unggah laporan kamu dalam format PDF:")
    uploaded_file = st.file_uploader("Pilih file PDF", type="pdf")

    if uploaded_file is not None:
        st.success(f"Berhasil mengunggah: **{uploaded_file.name}**")
        st.info("⚠️ Saat ini file belum tersimpan permanen (fitur simpan ke database masih dalam pengembangan).")

# ---------- Halaman KONTAK ----------
elif menu == "Kontak":
    st.subheader("📞 Kontak Admin / Dosen")
    st.markdown("""
    📧 **Email**: limbahedu@kampus.ac.id  
    📱 **WhatsApp**: [Klik untuk chat](https://wa.me/6281234567890)  
    🌐 **Website**: [limbahedu.streamlit.app](https://limbahedu.streamlit.app)
    """)
