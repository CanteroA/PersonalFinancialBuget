import streamlit as st
from datetime import datetime
import Database as db

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
        data = (
            banco, franquicia, categoria, digitos,
            dia_corte, dia_pago, cupo, tasa,
            int(cuota_manejo), int(beneficio_tasa)
        )
        ok, mensaje = db.insertarTarjeta(data)
        if ok:
            st.success(mensaje) 
        else:
            st.error(mensaje)

# Mostrar tabla de tarjetas registradas
st.subheader("💳 Tarjetas Registradas")
df = db.obtenerTarjetas()
st.dataframe(df)            