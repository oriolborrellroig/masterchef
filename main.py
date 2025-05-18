import streamlit as st
import re
from encrypter import VigenereCatala

st.title("MasterChef II: Encrypted edition🕵️‍♂️")

opcions = st.selectbox("Tria una acció:", ["Desencriptar", "Encriptar"])
clau = st.text_input("Clau").upper().replace(" ", "")
text = st.text_area("Text 2", height=400)  # quadre més alt

v = VigenereCatala(clau)

def capitalitza_frases(text):
    # Primer, tot a minúscules
    text = text.lower()
    # Capitalitza després de punt seguit o inici de paràgraf
    frases = re.split('(?<=[.!?]) +', text)
    frases = [f.capitalize() for f in frases]
    return ' '.join(frases)


if st.button("Executa"):
    if opcions == "Encriptar":
        resultat = v.vigenere(text, clau, encripta=True)
        resultat = capitalitza_frases(resultat)
        st.write("Resultat:\n", resultat)
    elif opcions == "Desencriptar":
        resultat = v.vigenere(text, clau, encripta=False, barreja_majuscules=False)
        resultat = capitalitza_frases(resultat)
        st.write("Resultat:\n", resultat)
    else:
        st.write("Algo ha anat malament, torna a intentar")
