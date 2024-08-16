import json
from google.cloud import storage
import pandas as pd
import glob
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import bigquery
import io
from datetime import datetime



# Creacion de una funcion que lee archivos de airflow y los sube a otro bucket

def upload_df_to_gcs():
    states = ["louisiana","indiana"]
    month = datetime.now().strftime("%B").lower()
     # Create an in-memory buffer
    buffer = io.BytesIO()
    for state in states:
        try:
            archivo = pd.read_json(f"/home/airflow/gcs/dags/{state}/{month}.json",encoding="utf-8", lines=True)
            # Convertimos microsegundos fecha y agregamos una columna con el valor
            archivo["date"] = pd.to_datetime(archivo["time"], unit='ms').astype("date64[pyarrow]")
            archivo.drop(columns=["pics","resp","time","name"],inplace=True)

            # Write the DataFrame to the buffer as Parquet
            archivo.to_parquet(buffer, engine='pyarrow')
            # Load data from Cloud Storage to BigQuery
            client = bigquery.Client()
            job_config = bigquery.job.LoadJobConfig()
            job_config.create_disposition = "CREATE_IF_NEEDED"
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND 
            table = f"{state}.reviews"
            job = client.load_table_from_dataframe(archivo,table,job_config=job_config)
        except:
            print("Data no available ")
    



upload_df_to_gcs()
