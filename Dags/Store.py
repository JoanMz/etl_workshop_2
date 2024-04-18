from decouple import config
from datetime import datetime
import logging
import sys
sys.append("../Drive")
import ApiDrive

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Store:logs]")

def Store_data():
    try:
        logger.log(level=20, msg=f"[{datetime.now()}] - start Drive_api")
        ApiDrive.Upload_file("../Data/clean_data/merge.csv")
        logger.log(level=20, msg=f"[{datetime.now()}] - finish store")

    except Exception as err:
        logger.error(f"[{datetime.now()}] - {err}")
