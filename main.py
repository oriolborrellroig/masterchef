import streamlit as st

st.title("Transformador de Text")

input1 = st.text_input("Text 1")
input2 = st.text_input("Text 2")

if st.button("Transforma"):
    resultat = (input1 + " " + input2).upper()  # Exemple simple
    st.write("Resultat:", resultat)
