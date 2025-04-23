import streamlit as st

st.title("MasterChef II: Encrypted edition🕵️‍♂️")


# Exemple simple
users = {
    "usuari1": "contrasenya123",
    "maria": "1234"
}

st.title("Login")

usuari = st.text_input("Usuari")
contrasenya = st.text_input("Contrasenya", type="password")

if st.button("Entrar"):
    if usuari in users and users[usuari] == contrasenya:
        st.success("Benvingut, " + usuari)
        # Aquí pots posar la teva app

        opcions = st.selectbox("Tria una acció:", ["Encriptar", "Desencriptar"])
        clau = st.text_input("Clau")
        text = st.text_area("Text 2", height=400)  # quadre més alt

        if st.button("Executa"):
            resultat = (clau + " " + text).upper()  # Exemple simple
            # st.write("Resultat:\n", resultat)
            st.write("Resultat:\n", "Aquesta web encara no està disponible. Trenca't una mica el cap, va" )

    else:
        st.error("Credencials incorrectes")
