import streamlit as st

st.title("MasterChef II: Encrypted edition🕵️‍♂️")


# Exemple simple
users = {
    "usuari1": "contrasenya123",
    "maria": "1234"
}

st.subheader("User")

col1, col2 = st.columns(2)

with col1:
    user = st.text_input("Usuari")

with col2:
    password = st.text_input("Contrasenya", type="password")
    

st.subheader("Text")

opcions = st.selectbox("Tria una acció:", ["Encriptar", "Desencriptar"])
clau = st.text_input("Clau")
text = st.text_area("Text 2", height=200)  # quadre més alt

if st.button("Executa"):
    if user in users and users[user] == password:
        resultat = (clau + " " + text).upper()  # Exemple simple
        # st.write("Resultat:\n", resultat)
        st.write("Resultat:\n", "Aquesta web encara no està disponible. Trenca't una mica el cap, va" )

    else:
        st.error("Credencials incorrectes")
