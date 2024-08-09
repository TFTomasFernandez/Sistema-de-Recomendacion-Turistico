from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
 

    storage_client = storage.Client(project="cosmic-carving-431013-c0")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")


upload_blob("testing-airflow","secFake.json","demo.csv")


import json
from google.cloud import storage
import chardet

def combine_json_files():
    """Combines multiple JSON files into a single JSON array.

    Args:
        event (dict): The Cloud Functions event data.
        context (google.cloud.functions.Context): Metadata for the event.
    """

    bucket_name = "testing-airflow"  # Replace with your bucket name
    prefix = "/*.json"  # Replace with the prefix for your files

    storage_client = storage.Client(project="cosmic-carving-431013-c0")
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()

    combined_data = []
    for blob in blobs:
        # print(blob)
        # blob_data = blob.download_as_bytes()
        # data = json.loads(blob_data)
        # combined_data.extend(data)
        try:
          file = bucket.get_blob(f"{blob.name}")
          blob_data = file.download_as_string()
          # Assuming UTF-8 encoding
          decoded_data = blob_data.decode('utf-8')
          data = json.loads(decoded_data)
          combined_data.extend(data)
        except Exception as e:
          print(f"Error processing file {blob.name}: {e}")

    # Create a new blob for the combined data
    output_blob_name = "combined_data.json"
    output_blob = bucket.blob(output_blob_name)
    output_blob.upload_from_string(json.dumps(combined_data))

    print(f"Combined data uploaded to {output_blob_name}")


# combine_json_files()