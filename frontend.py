import streamlit as st

st.set_page_config(
    page_title="QR Generator",
    page_icon="🏿",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: black;'>QR Generator</h1>", unsafe_allow_html=True)

with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        with st.form('Enter Product Details'):
            pass

    with right_col:
        st.title('The Generated QR Will Appear Here')
