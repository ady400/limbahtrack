import streamlit as st

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
