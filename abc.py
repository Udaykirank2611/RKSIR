import streamlit as st
st.title("View PDF from Google Drive")
pdf_url = "https://drive.google.com/file/d/1Ey7_UDgxJWoy7ZEzp3ulfXkRrtBGtHZT/view?usp=drive_link"
st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={pdf_url}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)