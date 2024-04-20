from datetime import datetime
import json
import logging
import pandas as pd
import sys
sys.path.append("/home/joan/Desktop/etl_workshop_2/DB_Connection")
import Pysqlconnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Load:logs]")

def load_to_postgres(**keywargs)->None:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start load to postgres")
        ti = keywargs["ti"]
        json_merge = json.loads(ti.xcom_pull(task_ids="merge_dataset"))
        df = pd.json_normalize(data=json_merge)
        df.to_sql("merge", Pysqlconnect.connection(),if_exists="replace", index_label="id")
        df.to_csv("/home/joan/Desktop/etl_workshop_2/Data/clean_data/merge.csv")
        logger.log(level=20, msg=f"[{datetime.now()}] - data loaded")
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")
        sys.exit(1)



#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger("[Load:logs]")
#
#def load_to_postgres(df:pd.DataFrame)->None:
#    try:
#        logger.log(level=20, msg=f"[{datetime.now()}] - start load to postgres")
#        df.to_sql("merge", if_exists="replace", index_label="id")
#        logger.log(level=20, msg=f"[{datetime.now()}] - data loaded")
#    except Exception as err:
#        logger.error(msg=f"[{datetime.now()}] - {err}")
