import streamlit as st
import pandas as pd
from docx import Document

st.set_page_config(page_title="WasteVisual", layout="wide")
st.title("WasteVisual: Visualisasi Data Limbah Industri")

# Upload file Word
uploaded_file = st.file_uploader("Unggah file Word (.docx) berisi tabel limbah")

def read_word_table(file):
    doc = Document(file)
    data = []
    for table in doc.tables:
        headers = [cell.text.strip() for cell in table.rows[0].cells]
        for row in table.rows[1:]:
            values = [cell.text.strip() for cell in row.cells]
            data.append(dict(zip(headers, values)))
        break  # Hanya baca tabel pertama
    return pd.DataFrame(data)

# Tampilkan data
if uploaded_file:
    try:
        df = read_word_table(uploaded_file)
        st.subheader("Data Limbah yang Diunggah:")
        st.dataframe(df)

        # Contoh visualisasi sederhana (jika ada kolom 'Tanggal' dan 'COD')
        if 'Tanggal' in df.columns and 'COD' in df.columns:
            df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')
            df['COD'] = pd.to_numeric(df['COD'], errors='coerce')
            st.line_chart(df.set_index('Tanggal')['COD'])
    except Exception as e:
        st.error(f"Gagal memproses file: {e}")
else:
    st.info("Silakan unggah file Word berisi tabel data limbah.")
