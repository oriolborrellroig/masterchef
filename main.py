import streamlit as st

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

    with st.sidebar:
        st.title("🎈 Okld's Gallery")

    st.subheader("User")

    col1, col2 = st.columns(2)

    with col1:
        user = st.text_input("Usuari")

    with col2:
        password = st.text_input("Contrasenya", type="password")


def main():

    with st.sidebar:
        st.title("🎈 Okld's Gallery")

        with st.expander("✨ APPS", True):
            user, password = load_login()
            load_text(user, password)

        with st.expander("🧩 COMPONENTS", True):
            st.title("🎈 Okld's Gallery")


if __name__ == "__main__":
    st.set_page_config(page_title="MasterChef II: Encrypted edition", page_icon="🕵️‍♂️", layout="wide")
    main()
