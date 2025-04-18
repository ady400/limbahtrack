import streamlit as st
from PIL import Image

# Menu "Beranda"
if menu == "Beranda":
    # Styling Header (judul)
    st.markdown("""
        <style>
            .title {
                text-align: center; 
                font-size: 36px; 
                font-weight: bold;
                color: #2E8B57;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                font-size: 18px;
                color: gray;
            }
        </style>
        <div class='title'>🌿 Aplikasi Edukasi Limbah Industri</div>
        <div class='subtitle'>Belajar lebih mudah, visual, dan menyenangkan!</div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Memastikan gambar ada di folder assets/
    img_path = "assets/beranda_canva.png"
    if os.path.exists(img_path):
        img = Image.open(img_path)
        st.image(img, use_container_width=True)
    else:
        st.error("Gambar tidak ditemukan di folder 'assets/'")

    st.markdown("---")

    # Info Box
    st.success("👋 Selamat datang! Aplikasi ini cocok untuk mahasiswa Teknik Lingkungan, Kimia, dan sejenisnya.")
    
    st.markdown("""
    ### 📌 Fitur Utama:
    - 📚 **Materi Edukatif** tentang pengolahan limbah industri
    - 🧮 **Kalkulator COD** untuk praktikum laboratorium
    - 📤 **Upload Laporan** langsung dari aplikasi
    - 📞 **Kontak Admin** jika kamu butuh bantuan
    """)

    st.info("💡 *Tips*: Gunakan menu di sidebar untuk menjelajahi fitur aplikasi ini.")
    st.markdown("---")

    # Call to Action
    st.markdown("<h4 style='color: orange;'>Siap belajar? Ayo mulai sekarang 🚀</h4>", unsafe_allow_html=True)
