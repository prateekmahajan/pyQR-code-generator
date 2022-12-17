import streamlit as st
from utilities import *
st.set_page_config(
    page_title="QR Generator",
    page_icon="🏿",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: black;'>QR Generator</h1>", unsafe_allow_html=True)

with st.container():
    with st.form('Enter Product Details'):
        field1 = st.text_input(label='field 1', placeholder='Enter Field Details Here')
        field2 = st.text_input(label='field 2', placeholder='Enter Field Details Here')
        field3 = st.text_input(label='field 3', placeholder='Enter Field Details Here')
        field4 = st.text_input(label='field 4', placeholder='Enter Field Details Here')
        field5 = st.text_input(label='field 5', placeholder='Enter Field Details Here')
        field6 = st.text_input(label='field 6', placeholder='Enter Field Details Here')
        field7 = st.text_input(label='field 7', placeholder='Enter Field Details Here')
        submitted = st.form_submit_button("Generate QR")
        if submitted:
            list_of_fields_for_qr_generation = [field1, field2, field3, field4, field5, field7]
            str_for_qr = ':'.join(list_of_fields_for_qr_generation)
            generate_qr(str_for_qr)
