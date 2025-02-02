import streamlit as st
st.title("View PDF from Google Drive")
pdf_url = "https://drive.google.com/file/d/1Ey7_UDgxJWoy7ZEzp3ulfXkRrtBGtHZT/preview"
pdf_display = f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>'
