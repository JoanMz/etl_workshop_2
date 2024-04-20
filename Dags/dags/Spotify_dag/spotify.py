from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append("/home/joan/Desktop/etl_workshop_2/Dags")
from Spotify import Extract as ExtractSpotify, drop_fake_index_col, drop_duplicates
from Grammys import Extract as ExtractGrammys, add_column_published_date, drop_columns, drop_nulls
from Merge import merge_data
from Load import load_to_postgres
from Store import Store_data


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Spotify-dag',
    default_args=default_args,
    description='Etl process to grammys analysis',
    schedule_interval=timedelta(days=1),
)

def log_task_execution(task_name, **kwargs):
    print(f"Executing task: {task_name}")

with dag:
    extract_spotify_task = PythonOperator(
        task_id='extract_spotify_task',
        python_callable=ExtractSpotify,
    )

    drop_fake_index_col_task = PythonOperator(
        task_id='drop_fake_index_col_task',
        python_callable=drop_fake_index_col,
    )

    drop_duplicates_task = PythonOperator(
        task_id='drop_duplicates_task',
        python_callable=drop_duplicates,
    )

    extract_grammys_task = PythonOperator(
        task_id='extract_grammys_task',
        python_callable=ExtractGrammys,
    )

    add_column_published_date_task = PythonOperator(
        task_id='add_column_published_date_task',
        python_callable=add_column_published_date,
    )

    drop_columns_task = PythonOperator(
        task_id='drop_columns_task',
        python_callable=drop_columns,
    )

    drop_nulls_task = PythonOperator(
        task_id='drop_nulls_task',
        python_callable=drop_nulls,
    )

    merge_dataset = PythonOperator(
        task_id='merge_dataset',
        python_callable=merge_data,
    )

    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_to_postgres,
    )

    Drive_upload = PythonOperator(
        task_id="Drive_upload",
        python_callable=Store_data,
    )


    extract_spotify_task >> drop_fake_index_col_task >> drop_duplicates_task >> merge_dataset
    extract_grammys_task >> add_column_published_date_task >> drop_columns_task >> drop_nulls_task >> merge_dataset
    merge_dataset >> load_data >> Drive_upload