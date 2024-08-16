import pandas as pd
import joblib
import funciones 
import warnings
warnings.filterwarnings('ignore')

df = pd.read_parquet('google_yelp_target.parquet',engine='pyarrow')

# Cargar múltiples objetos desde un archivo .pkl
with open('artefactos_mini.pkl', 'rb') as archivo:
    artefactos = joblib.load(archivo)

matriz = artefactos['matriz']
vectorizador = artefactos['vectorizer']

def rec_system(text):
    try:
        df_similarity = funciones.similaridad(df,text,vectorizador,matriz)
        df_rec = funciones.recomendar_ciudad(df_similarity)
        place = df_rec[df_rec["similarity_score"]==df_rec["similarity_score"].max()]
        return place
    except Exception:
        return  "error"
