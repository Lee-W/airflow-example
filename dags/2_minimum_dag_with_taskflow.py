from __future__ import annotations

from airflow.decorators import dag, task
from airflow.sdk import chain


@dag(
    schedule="0 0 * * *",
    catchup=False,
)
def example_dag():
    @task
    def parse_data():
        pass

    @task
    def process_data():
        pass

    @task
    def report():
        pass

    chain(parse_data(), process_data(), report())


example_dag()
