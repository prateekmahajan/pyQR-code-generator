import streamlit as st
from utilities import *

st.set_page_config(
    page_title="QR Generator",
    page_icon="🏿",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: white;'>QR Generator</h1>", unsafe_allow_html=True)

with st.container():
    _, mid_col, _ = st.columns([1, 2, 1])
    with mid_col:
        with st.form('Enter Product Details',clear_on_submit=True):
            field1 = st.text_input(label='field 1', placeholder='Enter Field Details Here')
            field2 = st.text_input(label='field 2', placeholder='Enter Field Details Here')
            field3 = st.text_input(label='field 3', placeholder='Enter Field Details Here')
            field4 = st.text_input(label='field 4', placeholder='Enter Field Details Here')
            field5 = st.text_input(label='field 5', placeholder='Enter Field Details Here')
            field6 = st.text_input(label='field 6', placeholder='Enter Field Details Here')
            field7 = st.text_input(label='field 7', placeholder='Enter Field Details Here')
            submitted = st.form_submit_button("Generate QR")
            if submitted:
                if len(field1) <= 0 or len(field2) <= 0 or len(field3) <= 0 or len(field4) <= 0 or len(
                        field5) <= 0 or len(field6) <= 0 or len(field7) <= 0:
                    st.error('All Fields Are Mandatory')
                else:
                    list_of_all_fields = [field1, field2, field3, field4, field5, field6, field7]
                    list_of_fields_for_qr_generation = [field1, field2, field3, field4, field5, field7]
                    str_for_qr = ':'.join(list_of_fields_for_qr_generation)
                    str_of_all_fields = ':'.join(list_of_all_fields)
                    try:
                        generate_qr(str_for_qr, str_of_all_fields)
                        st.success('QR Image Generated And Saved Successfully On your Device')
                    except Exception as e:
                        st.error("Something Went Wrong")
    _, mid_col, _ = st.columns([1, 0.5, 1])
    with mid_col:
        st.image('./sticker.png')
