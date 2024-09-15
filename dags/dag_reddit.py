from airflow.decorators import dag, task
import datetime

@dag(
    dag_id='dat_etl_reddit',
    schedule_interval='@daily',
    start_date=datetime.datetime(2024, 9, 15),
    catchup=False,
    default_args={
        'owner': 'Ruben Blanco',
        'retries': 1,
        'retry_delay': datetime.timedelta(minutes=10)
    },
    tags=['etl', 'reddit']
)
def reddit_elt_dag():
    
    @task
    def etl_reddit_data():
        pass

    etl_reddit_data()

dag_instance  = reddit_elt_dag()