from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='simple_test_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['test'],
) as dag:
    start_task = BashOperator(
        task_id='start',
        bash_command='echo "Hello from Airflow!"',
    )