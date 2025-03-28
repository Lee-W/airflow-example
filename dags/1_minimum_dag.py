from __future__ import annotations

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG


def parse_data():
    pass


def process_data():
    pass


def plot():
    pass


def report():
    pass


with DAG(
    dag_id="example_dag_1",
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    parse_data_task = PythonOperator(task_id="parse_data", python_callable=parse_data)
    prcess_data_task = PythonOperator(
        task_id="process_data", python_callable=process_data
    )
    report_task = PythonOperator(task_id="report", python_callable=report)

    parse_data_task >> prcess_data_task >> report_task
