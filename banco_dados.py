import sqlite3
import pandas as pd

DB="data/soc_transparencia.db"

def conectar():
    return sqlite3.connect(DB)

def salvar_tabela(nome,df):

    conn=conectar()

    df.to_sql(nome,conn,if_exists="replace",index=False)

    conn.close()

def carregar_tabela(nome):

    conn=conectar()

    try:
        df=pd.read_sql(f"SELECT * FROM {nome}",conn)
    except:
        df=pd.DataFrame()

    conn.close()

    return df
