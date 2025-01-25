from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providrs.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

# Define the DAG
with DAG(
    dag_id="nasa_apod_postgres",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    ## Step 1: Create the table if not exists
    @task
    def create_table():
        ## initialize the postgresHook
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        ## SQL Query to create the table
        create_table_query="""
        CREATE TABLE IF NOT EXISTS apod-data (
            id SERIAL PRIMARY KEY,
            title VARCHAR(200),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """
        ## Execute the table creation query
        postgres_hook.run(create_table_query)
    ## Step 2: Extract the NASA API Data (APOD) - Astronomy Picture of the Day [Extract pipeline]


    ## Step 3: Transform the data [Pick the information that i need to save]


    ## Step 4: Load the data into the Postgres database [Load pipeline]


    ## Step 5: Vérify the data DBViewer

    ## Step 6: Define the task dependencies