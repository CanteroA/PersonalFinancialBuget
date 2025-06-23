from supabase import create_client, Client
import streamlit as st
from config import SUPABASE_URL,SUPABASE_KEY


supabase: Client = create_client(SUPABASE_URL,SUPABASE_KEY)

def loginUser(email: str, password: str):
    try:
        response = supabase.auth.sign_in_with_password({"email":email,"password":password})
        if response.user:
            return response
        else:
            st.error("Credenciales incorrectas o usuario no existe")
    except Exception as e:
        st.error("Error al intentar iniciar sesion")
        return None
    
def logoutUser():
    st.session_state.clear()
    st.rerun()