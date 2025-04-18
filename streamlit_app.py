import streamlit as 

Konfigurasi halaman

st.set_page_config( page_title="Aplikasi Edukasi Limbah Industri", page_icon="♻️", layout="centered" )

Gaya CSS tambahan untuk mempercantik

st.markdown(""" <style> .title { font-size: 40px; font-weight: 700; color: #2ECC71; text-align: center; margin-top: 20px; } .subtitle { font-size: 20px; color: #ffffff; text-align: center; } .box { background-color: #1B2631; padding: 20px; border-radius: 15px; margin: 20px 0; color: #D5D8DC; box-shadow: 0 4px 8px rgba(0,0,0,0.2); } .emoji { font-size: 30px; } </style> """, unsafe_allow_html=True)

Header

st.markdown('<div class="title">♻️ Selamat Datang di Aplikasi Edukasi Limbah Industri</div>', unsafe_allow_html=True) st.markdown('<div class="subtitle">Belajar pengolahan limbah industri kini lebih mudah dan menyenangkan!</div>', unsafe_allow_html=True)

st.markdown("---")

Box informasi utama

st.markdown('<div class="box">✅ Aplikasi ini dirancang untuk mahasiswa Teknik Lingkungan dan pemula yang ingin belajar proses pengolahan limbah industri dengan cara yang interaktif.</div>', unsafe_allow_html=True)

Tips penggunaan

st.markdown('<div class="emoji">📌</div> <h4>Tips Menggunakan Aplikasi Ini:</h4>', unsafe_allow_html=True) st.markdown("""

Navigasikan materi melalui sidebar di kiri layar.

Gunakan Kalkulator COD untuk bantu hitung parameter laboratorium.

Klik menu Quiz & Fakta untuk menguji pemahamanmu.

Akses gambar proses limbah di tiap bagian materi. """)


Footer kecil

st.markdown("""

<center><sub>© 2025 - EduLimbahStream | Dibuat untuk pembelajaran</sub></center>
""")
