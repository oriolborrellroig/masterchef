import streamlit as st

st.title("MasterChef II: Encrypted edition")

input1 = st.text_input("Clau")
input2 = st.text_area("Text")

if st.button("Executa"):
    resultat = (input1 + " " + input2).upper()  # Exemple simple
    st.write("Resultat:", resultat)
