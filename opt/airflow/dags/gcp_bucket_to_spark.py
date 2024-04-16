import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.sensors.gcs import GCSObjectsWithPrefixExistenceSensor
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


bucket_name = os.getenv('BUCKET_NAME', 'default-fallback-bucket')
bigquery_dataset = os.getenv('BIGQUERY_DATASET', 'ships_ds') 
project_id = os.getenv('PROJECT_ID') 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'gcs_file_sensor_dag',
    default_args=default_args,
    description='A DAG to sense for a file in GCS and trigger Spark job',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

sense_file = GCSObjectsWithPrefixExistenceSensor(
    task_id='sense_file_in_gcs',
    bucket=bucket_name,
    prefix='',  
    google_cloud_conn_id='gcp_connection',
    dag=dag,
)

submit_spark_job = SparkSubmitOperator(
    task_id='submit_spark_job',
    application='/opt/bitnami/spark-jobs/spark_job.py',
    conn_id='spark_default',
    executor_cores='1',
    jars='/opt/bitnami/spark/jars/gcs-connector-hadoop3-latest.jar,/opt/bitnami/spark/jars/spark-3.4-bigquery-0.37.0.jar',
    application_args=[f'gs://{bucket_name}/small_test_data.csv', f'{project_id}:{bigquery_dataset}:ships_table'],
    conf={
        'spark.hadoop.fs.gs.impl': 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem',
        'spark.hadoop.fs.gs.auth.service.account.enable': 'true',
        'spark.hadoop.fs.gs.auth.service.account.json.keyfile': '/opt/bitnami/config/gcp-key.json',
        'spark.executor.heartbeatInterval': '120s',
        'spark.network.timeout' :'500s',
        'spark.worker.timeout' :'500s'
    },
    dag=dag,
)

sense_file >> submit_spark_job