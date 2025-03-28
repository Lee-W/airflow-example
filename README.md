# apache-airflow 3.0.0dev example

## Getting Started

### Prerequisites

* [uv](https://docs.astral.sh/uv/)
* docker

### Setup

```shell
git clone https://github.com/apache/airflow/
cd airflow/
uv tool install -e ./dev/breeze --python 3.12
uv tool install pre-commit --python 3.12

# move the "dags" directory in this repo to "files/dags" in the cloned airflow repo

breeze compile-ui-assets
breeze start-airflow --db-reset
```
Open `http://localhost:28080/` to access the airflow web interface
The default username / password for testing are both "admin". 

## Authors

[Lee-W](https://github.com/Lee-W)
