from datetime import datetime
import pandas as pd
from pytz import timezone
import logging
import traceback
from config import *
from paw_eth_stats_crud import session



set_logger(logging)
est_tz = timezone('EST')


def read_eth_price_db():
    try:
        logging.info("----In read_eth_price_db read from eth_price table and load into csv----")
        s = session()
        df = pd.read_sql(sql=sql_eth_price,con=s.bind)
        print(df.head())
        #save to local csv folder
        dtnow = datetime.now(est_tz).date()
        
        csv_name = 'eth_daily_price_stats_'+ str(dtnow) +'.csv'
        csv_name = csv_save_path + csv_name
        df.to_csv(path_or_buf = csv_name,sep = ',',index = False)
    except Exception as e:
        logging.error(("There is issue in reading/loding data into csv! " + str(e)))    

if __name__ == '__main__':
    try:
        logging.info("----Read data from eth_price table and load csv----")
        
        #read data from db
        read_eth_price_db()

    except Exception as e:
        logging.error(traceback.print_exc())
        logging.error("Error in Read data from eth_stats and loading to csv .Please check! " + str(e))
        raise Exception(e)
        
