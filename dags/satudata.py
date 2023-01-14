from airflow.decorators import dag, task
import pendulum

TASK_RETRIES = 2

@task(retries=TASK_RETRIES)
def etl_pusdatin_arsip_dbo_pd() -> dict:
    return {}

@task
def etl_pddikti_pddikti_dbo_5() -> dict:
    return {}

@task
def etl_pddikti_pddikti_dbo_7() -> dict:
    return {}

@task
def dbt_satu_data_dev() -> dict:
    return {}

@task
def dbt_satu_data_master_pii() -> dict:
    return {}

@task
def dbt_satu_data_master() -> dict:
    return {}


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def run_workflow():
    etl_pusdatin_arsip_dbo_pd_task = etl_pusdatin_arsip_dbo_pd()
    etl_pddikti_pddikti_dbo_5_task = etl_pddikti_pddikti_dbo_5()
    etl_pddikti_pddikti_dbo_7_task = etl_pddikti_pddikti_dbo_7()
    dbt_satu_data_dev_task = dbt_satu_data_dev()
    dbt_satu_data_master_pii_task = dbt_satu_data_master_pii()
    dbt_satu_data_master_task = dbt_satu_data_master()
    
    etl_pusdatin_arsip_dbo_pd_task >> dbt_satu_data_dev_task >> dbt_satu_data_master_pii_task
    etl_pddikti_pddikti_dbo_5_task >> dbt_satu_data_master_pii_task
    etl_pddikti_pddikti_dbo_7_task >> dbt_satu_data_master_pii_task
    dbt_satu_data_master_pii_task >> dbt_satu_data_master_task
    etl_pddikti_pddikti_dbo_7_task >> dbt_satu_data_master_task

run_workflow()