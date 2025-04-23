import streamlit as st

st.title("MasterChef II: Encrypted edition")

opcions = st.radio("Tria una acció:", ["Majúscules", "Minúscules", "Title Case"])
clau = st.text_input("Clau")
text = st.text_area("Text 2", height=400)  # quadre més alt

if st.button("Executa"):
    resultat = (input1 + " " + input2).upper()  # Exemple simple
    st.write("Resultat:\n", resultat)
