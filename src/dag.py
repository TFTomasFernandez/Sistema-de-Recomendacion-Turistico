from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
# from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 8),
    'depends_on_past': False,
    'email': ['tinchoferrarigd@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data-forge',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@monthly',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='states',
        bash_command='python /home/airflow/gcs/dags/scripts/combined.py',
    )
    run_script_business = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/business_etl.py',
    )

    run_script_task >> run_script_business

    # start_pipeline = CloudDataFusionStartPipelineOperator(
    # location="us-central1",
    # pipeline_name="etl-pipeline",
    # instance_name="datafusion-dev",
    # task_id="start_datafusion_pipeline",
    # )