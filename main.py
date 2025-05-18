import streamlit as st
from encrypter import VigenereCatala

st.title("MasterChef II: Encrypted edition🕵️‍♂️")

opcions = st.selectbox("Tria una acció:", ["Desencriptar", "Encriptar"])
clau = st.text_input("Clau").upper().replace(" ", "")
text = st.text_area("Text 2", height=400)  # quadre més alt

v = VigenereCatala(clau)


if st.button("Executa"):
    if opcions == "Encriptar":
        resultat = v.vigenere(text, clau, encripta=True)
        st.write("Resultat:\n", resultat)
    elif opcions == "Desencriptar":
        resultat = v.vigenere(text, clau, encripta=False, barreja_majuscules=False)
        st.write("Resultat:\n", resultat)
    else:
        st.write("Algo ha anat malament, torna a intentar")
