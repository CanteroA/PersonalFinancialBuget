import streamlit as st
import Database as db
from datetime import datetime
import supabase
import pandas as pd

def creditCardsInfo(user: str,
                    conn):
    st.title('Registro de tarjetas')

    with st.form('Registro tarjetas'):
        banco = st.text_input("Banco")
        franquicia = st.selectbox("Franquicia", ['VISA','MASTERCARD','AMEX'])
        categoria = st.selectbox("Categoria", ['BLACK','GOLD','PLATINUM'])
        digitos = st.number_input("Últimos 4 dígitos",min_value=0,max_value=9999,step=1)
        dia_corte = st.number_input("Día de corte", min_value=1, max_value=31)
        dia_pago = st.number_input("Día de pago", min_value=1, max_value=31)
        cupo = st.number_input("Cupo total", step=100000)
        tasa = st.number_input("Tasa actual (%)", step=0.1)
        cuota_manejo = st.checkbox("Tiene cuota de manejo")
        beneficio_tasa = st.checkbox("Tiene beneficio de tasa")

        enviado = st.form_submit_button("Registrar")


        if enviado:

            data = {
                'user':user,
                'banc':banco,
                'cc_network':franquicia,
                'cc_category':categoria,
                'last_digits':digitos,
                'billing.day':dia_corte,
                'payment_day':dia_pago,
                'credit_limit':cupo,
                'interest_rate':tasa,
                'deal_1':cuota_manejo,
                'deal_2':beneficio_tasa
            }

            try: 
                resp = conn.table('TarjetasCredito').insert(data).execute()
                st.success("💳 Tarjetas Registradas")
            except Exception as e:
                st.error(f"Error al registrar: {e}")

    # Mostrar tabla de tarjetas registradas
    st.subheader("💳 Tarjetas Registradas")
    df = conn.table('TarjetasCredito').select("*").eq("user",user).execute()
    df = pd.DataFrame(df)
    st.dataframe(df)