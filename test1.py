import streamlit as st

st.image('vignan.jpg', width=250)

task = st.selectbox("Menu", ["Data Profiler", "Data Quality Detector",
                                 "Data Corrector", "Review Summary Report and Download Adjusted Data", "Contact Us"])

with st.sidebar.subheader('Upload your file'):
    uploaded_file = st.sidebar.file_uploader("Please upload a file of type: xlsx, csv", type=["xlsx", "csv"])

st.sidebar.markdown("Made by Vignan/CSE",unsafe_allow_html=True)