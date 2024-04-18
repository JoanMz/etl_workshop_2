import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Spotify:logs]")

def Extract()->pd.DataFrame:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start Extract")
        df = pd.read_csv("../Data/spotify_dataset.csv")
        logger.log(level=20, msg=f"[{datetime.now()}] - data extracted")
        return df
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")


def drop_fake_index_col(df:pd.DataFrame)->pd.DataFrame:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start drop_fake_index")
        df.drop(columns=("Unamed: 0"), inplace=True)
        logger.log(level=20, msg=f"[{datetime.now()}] - finish drop_fake_index")
        return df
    except Exception as err:
        logger.error(f"[{datetime.now()}] - {err}")
        

def drop_duplicates(df:pd.DataFrame)->pd.DataFrame:
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start drop duplicates")
        df.drop_duplicates(inplace=True)
        df = df[df["track_id"].duplicated() == False]
        logger.log(level=20, msg=f"[{datetime.now()}] - finish drop duplicates")
        return df
    except Exception as err:
        logger.error(msg=f"[{datetime.now()}] - {err}")



if __name__ == "__main__":
    print("test")
    Extract()