# apache-airflow beta4 example

## Getting Started

### Prerequisites

* [uv](https://docs.astral.sh/uv/)

### Usage

```shell
uv sync

# issue found in standalone command, but already fixed in the main branch
mv patch/standalone_command.py .venv/lib/python3.12/site-packages/airflow/cli/commands/local_commands/standalone_command.py

export AIRFLOW_HOME=`pwd`
uv run airflow db migrate
uv run airflow standalone

```

A `simple_auth_manager_passwords.json.generated` file will be generated. That's the default admin user name and password for you to login the web server on `http://localhost:8080/`

## Authors

[Lee-W](https://github.com/Lee-W)
