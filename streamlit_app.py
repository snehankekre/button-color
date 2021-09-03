import streamlit as st
import os

st.write(os.getcwd())

with st.echo():
    colors = st.radio(
        "Pick a color", ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    )

    s = f"""
    <style>
    div.stButton > button:first-child {{ background-color: {colors};}}
    <style>
    """
    st.markdown(s, unsafe_allow_html=True)

    st.button("Click me")
