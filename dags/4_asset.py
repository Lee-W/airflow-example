from __future__ import annotations

from airflow.decorators import dag, task
from airflow.sdk import Asset, AssetAlias

asset1 = Asset(name="asset1")
asset2 = Asset(name="asset2")

alias = AssetAlias(name="example_alias")


@dag(schedule=None, catchup=False)
def example_dag():
    @task(outlets=[alias])
    def parse_data(*, outlet_events) -> None:
        # assuming this is the result from parsed data
        asset_1_updated = True
        asset_2_updated = False

        if asset_1_updated:
            outlet_events[alias].add(asset1)

        if asset_2_updated:
            outlet_events[alias].add(asset2)

    parse_data()


@dag(schedule=asset1 & asset2, catchup=False)
def leaf_dag_1():
    @task
    def leaf_task():
        pass

    leaf_task()


@dag(schedule=asset1, catchup=False)
def leaf_dag_2():
    @task
    def leaf_task():
        pass

    leaf_task()


example_dag()
leaf_dag_1()
leaf_dag_2()
