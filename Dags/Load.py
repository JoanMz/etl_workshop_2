from datetime import datetime
import logging
import pandas as pd
import sys
sys.path.append("/home/joan/Desktop/etl_workshop_2/DB_Connection")
import Pysqlconnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Load:logs]")

def load_to_postgres(df:pd.DataFrame)->None:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start load to postgres")
        df.to_sql("merge", if_exists="replace", index_label="id")
        logger.log(level=20, msg=f"[{datetime.now()}] - data loaded")
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")
