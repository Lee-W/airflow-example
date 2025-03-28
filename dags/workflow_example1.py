from __future__ import annotations

from airflow.decorators import dag, task


@dag(
    schedule=None,
    catchup=False,
)
def example_dag_5():
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

    task1()
    task2()
    task3()
    task4()


example_dag_5()
