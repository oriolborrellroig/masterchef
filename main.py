import streamlit as st
import pandas as pd


users = {
    "usuari1": "contrasenya123",
    "maria": "1234"
}

    
def load_text (user, password):
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


def load_login ():
    # Exemple simple

    st.subheader("User")

    col1, col2 = st.columns(2)

    with col1:
        user = st.text_input("Usuari")

    with col2:
        password = st.text_input("Contrasenya", type="password")
    return user, password

def load_sidebar():
    data = pd.DataFrame({
        "Clau": ["AAAA", "BBBB", "CCCC"],
        "Text": ["AAAAAAAAAAAAAAAAAAAA", "BBBBBBBBBBBBBBBBBBBB", "CCCCCCCCCCCCCCCCCCCC"]
    })
    
    st.table(data)


def main():

    with st.sidebar:
        st.title("📖 Historial")
        load_sidebar()
    
    user, password = load_login()
    load_text(user, password)


if __name__ == "__main__":
    st.set_page_config(page_title="MasterChef II: Encrypted edition", page_icon="🕵️‍♂️")
    st.title("MasterChef II: Encrypted edition")
    main()
