import logging
from datetime import datetime
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Grammys:logs]")


def merge_data(df_grammys, df_spotify):
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start merge")
        df_merge = pd.merge(df_grammys, df_spotify, 
                            left_on="nominee", 
                            right_on="track_name", 
                            how="inner")
        logger.log(level=20, msg=f"[{datetime.now()}] - finish merge")

        logger.log(level=20, msg=f"[{datetime.now()}] - start drop columns")
        df_merge.drop(columns=("nominee"),inplace=True)
        df_merge.to_csv("../Data/clean_data/merge.csv")
        return df_merge
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")