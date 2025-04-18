import streamlit as st
from PIL import Image

# CONFIGURASI HALAMAN
st.set_page_config(page_title="Edukasi Limbah Industri", layout="wide", page_icon="♻️")

# HEADER UTAMA
st.markdown(
    """
    <div style='text-align: center; padding: 20px 0'>
        <h1 style='color: green;'>♻️ Aplikasi Edukasi Limbah Industri</h1>
        <p style='font-size: 18px;'>Belajar mengelola limbah industri jadi lebih mudah dan menyenangkan!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# TABS LAYOUT
tab1, tab2, tab3, tab4 = st.tabs(["🏭 Edukasi", "🧮 Kalkulator", "💡 Tips & Fakta", "📸 Galeri"])

# TAB 1 - EDUKASI
with tab1:
    st.subheader("Apa Itu Limbah Industri?")
    st.write("""
        Limbah industri adalah sisa hasil dari aktivitas produksi pabrik yang bisa berbentuk cair, padat, atau gas. 
        Jika tidak dikelola dengan baik, limbah ini bisa mencemari lingkungan dan membahayakan kesehatan manusia.
    """)

    st.markdown("### Jenis Pengolahan:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("*Fisik*")
        st.image("https://img.icons8.com/color/96/filters.png", width=50)
        st.write("Contoh: sedimentasi, penyaringan")
    with col2:
        st.markdown("*Kimia*")
        st.image("https://img.icons8.com/color/96/test-tube.png", width=50)
        st.write("Contoh: koagulasi, netralisasi")
    with col3:
        st.markdown("*Biologi*")
        st.image("https://img.icons8.com/color/96/eco.png", width=50)
        st.write("Contoh: pengolahan aerob & anaerob")

# TAB 2 - KALKULATOR COD
with tab2:
    st.subheader("Kalkulator Beban COD")

    volume = st.number_input("Masukkan Volume Air Limbah (liter)", min_value=0.0, step=0.1)
    konsentrasi = st.number_input("Masukkan Konsentrasi COD (mg/L)", min_value=0.0, step=0.1)

    if st.button("Hitung COD"):
        cod = volume * konsentrasi / 1000  # dalam gram
        st.success(f"Beban COD = {cod:.2f} gram")

# TAB 3 - TIPS
with tab3:
    st.subheader("Tips & Fakta Pengolahan Limbah")

    st.markdown("""
    - ✅ Gunakan metode kombinasi (fisik, kimia, biologi) untuk efisiensi tinggi.
    - ✅ Selalu pantau parameter penting seperti pH, suhu, COD, dan BOD.
    - ✅ Edukasi karyawan pabrik agar lebih peduli terhadap lingkungan.
    - ✅ Terapkan prinsip reduce, reuse, recycle (3R).

    *Tahukah kamu?*  
    Limbah dari industri makanan dan minuman tergolong lebih mudah diolah secara biologis dibanding limbah tekstil!
    """)

# TAB 4 - GALERI
with tab4:
    st.subheader("Galeri Limbah Industri")
    st.image("https://images.unsplash.com/photo-1581091012184-7f831f3a0c6f", caption="Proses di Pabrik", use_column_width=True)
    st.image("https://images.unsplash.com/photo-1589187155940-61150b927da2", caption="Pengolahan Air Limbah", use_column_width=True)

# SIDEBAR
st.sidebar.title("Navigasi")
st.sidebar.info("Pilih tab di atas untuk menjelajahi fitur aplikasi.")
st.sidebar.markdown("Made with ❤️ by [Nama Kamu]")
