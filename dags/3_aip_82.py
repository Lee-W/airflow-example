from __future__ import annotations

from airflow.decorators import dag, task
from airflow.providers.standard.triggers.file import FileDeleteTrigger
from airflow.sdk import Asset, AssetWatcher, chain

trigger = FileDeleteTrigger(filepath="/tmp/data")
example_data = Asset(
    name="example_data",
    watchers=[AssetWatcher(name="data_watcher", trigger=trigger)],
)


@dag(
    schedule=example_data,
    catchup=False,
)
def example_dag_3():
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


example_dag_3()
