import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from datetime import datetime
from creditCardsInfo import creditCardsInfo
from auth.login import loginUser, logoutUser
from db_supa import supabase_connector

supaConnection = supabase_connector()

st.set_page_config(page_title="My Intelligent Budget",layout="centered")


#Estado de sesion
if "user" not in st.session_state:
    st.session_state["user"] = None

#Login
if not st.session_state["user"]:
    st.title("My Intelligent Budget - Login")
    with st.form("loginForm"):
        email = st.text_input("E-mail:")
        password = st.text_input("Password",type="password")
        submitted = st.form_submit_button("Acceder")

        if submitted:
            ok = loginUser(email,password)
            if ok:
                st.rerun()
            else:
                st.error("Credenciales inválidas o usuario no registrado.")
                st.session_state["user"] = None
            
else:
    st.sidebar.title("Opciones")

    opcion = st.sidebar.radio("Selecciona una opcion:",[
        "Resumen general",
        "Gestion de tarjetas de credito",
        "Movimientos",
        "Cerrar sesion"
    ])

    if st.session_state["user"] is not None:
        st.sidebar.write("---")
        st.sidebar.success(f"Sesión: {st.session_state["user"]["email"]}")

    # Opciones

    if opcion == "Resumen general":
        st.title("📊 Resumen General")
        st.write("Aquí va tu dashboard de presupuestos, balances, etc.")

    elif opcion == "Gestion de tarjetas de credito":
        st.title("💳 Gestión de Tarjetas de Crédito")
        creditCardsInfo(user=st.session_state["user"]["id"], conn=supaConnection)

    elif opcion == "Movimientos":
        st.title("📒 Registro de movimientos")
        st.write("Aquí iría el CRUD de ingresos/gastos.")

    elif opcion == "Cerrar sesion":
        logoutUser()        