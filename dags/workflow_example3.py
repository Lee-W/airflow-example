from __future__ import annotations

from airflow.decorators import dag, task
from airflow.sdk import chain


@dag(
    schedule=None,
    catchup=False,
)
def example_dag():
    @task
    def task1():
        pass

    @task.branch
    def branch_task():
        import random

        return random.choice(["task2", "task3", "task4"])

    @task
    def task2():
        pass

    @task
    def task3():
        pass

    @task
    def task4():
        pass

    chain(task1(), branch_task(), [task2(), task3(), task4()])


example_dag()
