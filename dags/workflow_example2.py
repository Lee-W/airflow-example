from __future__ import annotations

from airflow.decorators import dag, task
from airflow.sdk import chain


@dag(
    schedule=None,
    catchup=False,
)
def example_dag_6():
    @task
    def task1():
        pass

    @task
    def task2():
        pass

    @task
    def task3():
        pass

    @task
    def task4():
        pass

    chain(task1(), task2(), [task3(), task4()])


example_dag_6()
