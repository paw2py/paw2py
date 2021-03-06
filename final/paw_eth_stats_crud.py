from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json
import requests
from datetime import datetime, timezone
import logging
import traceback
from config import *
from paw_tables import *



set_logger(logging)

try:
    engine = create_engine(DATABASE_URI)
    session = sessionmaker(bind=engine)
except Exception as e:
        logging.error("There is a issue while creating SQA Engine! " + str(e) )
        raise Exception(e)

#manager session for db
@contextmanager
def db_session():
    dbsession = session()
    try:
        yield dbsession
        dbsession.commit()
    except Exception as e:
        dbsession.rollback()
        logging.error("Error while commiting records " + str(e) ) 
        raise Exception(e)
    finally:
        dbsession.close()   


# fucntion to create all table in DB
def create_table():
    Base.metadata.create_all(bind=engine)

def read_eth_price_api():
    try:
        logging.info("----get ETH Latest price from stats API----")
        #stats url to get ETH latest price
        r = requests.get(eth_stats_price)
        if r.status_code == 200:
            return r.json()['result']
        else:
            raise Exception("ETH Latest Price API stats code != 200 " + str(r.starue_code))
    except Exception as e:
        logging.error("There is issue with ETH stats API url! " + str(e)) 
        raise Exception(e)
 
def load_eth_price_db(result):
    try:
        logging.info("----Load ETH latest price to eth_price table----")
        dt = datetime.now(timezone.utc)
        eth_price_data = eth_price(eth_btc = result['ethbtc'],
                                    eth_btc_tmstmp =  result['ethbtc_timestamp'],
                                    eth_usd = result['ethusd'],
                                    eth_usd_tmstmp = result['ethusd_timestamp'],
                                    update_id = 'pawethstats',
                                    update_tmstmp = dt
                                    )

        #load data to db eth_price table
        with db_session() as s:
            s.add(eth_price_data)
    except Exception as e:
        logging.error("Insert data into eth_price table failed! " + str(e))
        raise Exception(e)

if __name__ == '__main__':
    try:
        logging.info("----Create all table for ETH stats, gas and block----")
        create_table()
        eth_price_result = read_eth_price_api()
        load_eth_price_db(eth_price_result)

    except Exception as e:
        logging.error(traceback.print_exc())
        logging.error("Error in ETH api processing .Please check! " + str(e))
        raise Exception(e)
        
