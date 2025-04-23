import streamlit as st

st.title("MasterChef II: Encrypted edition🕵️‍♂️")

opcions = st.selectbox("Tria una acció:", ["Encriptar", "Desencriptar"])
clau = st.text_input("Clau")
text = st.text_area("Text 2", height=400)  # quadre més alt

if st.button("Executa"):
    resultat = (clau + " " + text).upper()  # Exemple simple
    # st.write("Resultat:\n", resultat)
    st.write("Resultat:\n", "Aquesta web encara no està disponible. Trenca't una mica el cap, va" )
