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
st.set_page_config(page_title="WasteVisual", layout="centered")
st.title("WasteVisual: Visualisasi Data Limbah Industri")

uploaded_file = st.file_uploader("Unggah file CSV berisi data limbah", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Limbah yang Diupload:")
    st.dataframe(df)

    st.subheader("Grafik COD")
    fig_cod = px.line(df, x='Tanggal', y='COD (mg/L)', markers=True, title="Tren COD")
    st.plotly_chart(fig_cod)

    st.subheader("Grafik BOD")
    fig_bod = px.line(df, x='Tanggal', y='BOD (mg/L)', markers=True, title="Tren BOD")
    st.plotly_chart(fig_bod)

    st.subheader("Analisis Kepatuhan Ambang Batas")
    cod_batas = 200
    bod_batas = 80

    cod_melebihi = df[df['COD (mg/L)'] > cod_batas]
    bod_melebihi = df[df['BOD (mg/L)'] > bod_batas]

    st.markdown(f"*Jumlah hari COD melebihi batas ({cod_batas} mg/L):* {len(cod_melebihi)}")
    st.markdown(f"*Jumlah hari BOD melebihi batas ({bod_batas} mg/L):* {len(bod_melebihi)}")

    if not cod_melebihi.empty:
        st.warning("Hari-hari dengan COD melebihi batas:")
        st.dataframe(cod_melebihi[['Tanggal', 'COD (mg/L)']])

    if not bod_melebihi.empty:
        st.warning("Hari-hari dengan BOD melebihi batas:")
        st.dataframe(bod_melebihi[['Tanggal', 'BOD (mg/L)']])
else:
    st.info("Silakan unggah file CSV terlebih dahulu.")
