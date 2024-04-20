import sys
sys.path.append("/home/joan/Desktop/etl_workshop_2/DB_Connection")
import Pysqlconnect
import pandas as pd
from datetime import datetime
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Grammys:logs]")


def Extract()->json:
    """This function load the data from postgres db to dataframe pandas"""
    try:
        df_grammys = pd.read_sql(sql="SELECT * FROM grammys;",  
                             con=Pysqlconnect.connection()) #load the data using own module
        logger.log(level=20, msg=f"[{datetime.now()}] - Postgres Connected  --- data-loaded ---")
        return df_grammys.to_json(orient="records")
    
    except Exception as err:
        logger.error(f"[{datetime.now()}]: {err}")
        return None


def datetime_transform(stdate:str)->datetime:
    """"This function is used for transform one string to datetime format sql"""
    try:
        date = datetime.strptime(stdate, '%Y-%m-%dT%H:%M:%S%z')
        formatdate = date.strftime('%Y-%m-%d') #this is the format to date to sql
        return formatdate
    except Exception as err:
        logger.error(f"[{datetime.now()}] - {err}")

def add_column_published_date(**kwargs:json)->json:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start 'add_column_published_date'")
        ti = kwargs["ti"]
        json_df = json.loads(ti.xcom_pull(task_ids="extract_grammys_task"))
        df = pd.json_normalize(data=json_df)
        df["published_date"] = df["published_at"].apply(datetime_transform)
        logger.log(level=20, msg=f"[{datetime.now()}] - finish task")
        return df.to_json(orient="records")
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")
        err

def drop_columns(**kwargs:json)->json:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start drop columns")
        ti = kwargs["ti"]
        json_df = json.loads(ti.xcom_pull(task_ids="add_column_published_date_task"))
        df = pd.json_normalize(data=json_df)
        df.drop(columns=["winner", "updated_at", "published_at", "workers", "img"], inplace=True)
        logger.log(level=20, msg=f"[{datetime.now()}] - columns droped")
        return df.to_json(orient="records")
    except Exception as err:
        logger.error(f"[{datetime.now()}] - {err}")

def drop_nulls(**kwargs:json)->json:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start drop nulls")
        ti = kwargs["ti"]
        json_df = json.loads(ti.xcom_pull(task_ids="drop_columns_task"))
        df = pd.json_normalize(data=json_df)
        df.dropna(inplace=True)
        logger.log(level=20, msg=f"[{datetime.now()}] - nulls droped")
        return df.to_json(orient="records")
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")

if __name__ == "__main__":
    df = Extract()
    datetime_transform(20)
    add_column_published_date(Extract())
    drop_columns(df)
    print(df.keys())    
    drop_nulls(df)
    print(df.notna().value_counts())

