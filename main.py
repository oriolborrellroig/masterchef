import streamlit as st
import re
import unicodedata
from encrypter import VigenereCatala

st.title("MasterChef II: Encrypted edition🕵️‍♂️")

def capitalitza_frases(text):
    # Primer, tot a minúscules
    text = text.lower()
    # Capitalitza després de punt seguit o inici de paràgraf
    frases = re.split('(?<=[.!?]) +', text)
    frases = [f.capitalize() for f in frases]
    return ' '.join(frases)

def elimina_accents(text):
    # Normalitza el text a la forma NFD (descomposa lletres + accents)
    text_normalitzat = unicodedata.normalize('NFD', text)
    # Elimina els caràcters amb categoria "Mn" (marca no espaiadora, com els accents)
    text_sense_accents = ''.join(c for c in text_normalitzat if unicodedata.category(c) != 'Mn')
    return text_sense_accents

def neteja_caracters_especials(text):
    # 1. Normalitza per treure accents i dièresis
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # 2. Elimina caràcters especials (només lletres i números si vols)
    text = re.sub(r'[^A-Za-z0-9 ]', '', text)
    return text

opcions = st.selectbox("Tria una acció:", ["Desencriptar", "Encriptar"])
clau = st.text_input("Clau").upper().replace(" ", "")
clau = elimina_accents(clau)
clau = neteja_caracters_especials(clau)
text = st.text_area("Text 2", height=300)  # quadre més alt

v = VigenereCatala(clau)

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
