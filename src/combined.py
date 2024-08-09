import json
from google.cloud import storage
import pandas as pd
import glob
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import bigquery
import io
from datetime import datetime


# path = "/home/airflow/gcs/dags/louisiana"

# Usamos glob para obtener todos los archivos JSON en el directorio
# all_files = glob.glob(f"{path}/*.json")

# df=[]
# for file in all_files:
# archivo = pd.read_json(lines=True,encoding="utf-8")

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
            archivo["date"] = pd.to_datetime(archivo["time"], unit='ms')
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






    # storage_client = storage.Client(project="cosmic-carving-431013-c0")
    # bucket = storage_client.bucket(bucket_name)
    # # destination_bucket = storage_client.bucket(final_bucket_name)
    # blob = bucket.blob(file_name)

    # # Upload the JSON data to the blob
    # blob.upload_from_string(buffer.getvalue(), content_type='application/octet-stream')


    # Delete all the files

    # blobs = bucket.list_blobs()
    # for blob in blobs:
    #     # blob.delete()
    #     break