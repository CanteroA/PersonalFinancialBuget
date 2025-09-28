from supabase import create_client, Client
import streamlit as st
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def loginUser(email: str, password: str) -> bool:
    try:
        resp = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if resp and resp.user:
            st.session_state["user"] = {
                "id": resp.user.id,
                "email": resp.user.email,
            }
            return True
        else:
            st.error("Credenciales incorrectas o usuario no existe")
            return False
    except Exception:
        st.error("Error al intentar iniciar sesión")
        return False

def logoutUser():
    st.session_state.clear()
    st.rerun()