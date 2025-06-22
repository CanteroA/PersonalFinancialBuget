import os
import sqlite3
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "presupuesto.db")


os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)


def obtenerTarjetas():
    return pd.read_sql("SELECT * FROM tarjetas", conn)

def insertarTarjeta(data):
    queryIstTarjeta = """INSERT INTO tarjetas(Banco, Franquicia, Categoria, Digitos, DiaCorte, DiaPago, Cupo, TasaActual, CuotaMenjo, BeneficioTasa)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        conn.execute(queryIstTarjeta,data)
        conn.commit()
        return True, "Adicionada"
    except sqlite3.Error as e:
        return False, "Error"


