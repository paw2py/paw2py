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
from paw_eth_stats_crud import db_session



set_logger(logging)

def read_eth_gas_oracle_api():
    try:
        logging.info("----get ETH Gas Oracle from get gas orale API----")
        #read gas oracle api        
        r = requests.get(eth_gas_oracle_api)
        if r.status_code == 200:
            return r.json()['result']
        else:
            raise Exception("ETH Gas Oracle API stats code != 200 " + str(r.starue_code))
    except Exception as e:
        logging.error("There is issue with ETH Gas Oracle url! " + str(e)) 
        raise Exception(e)
 
def load_eth_gas_oracle_db(result):
    try:
        logging.info("----Load ETH Gas Oracle to eth_gas_oracle table----")
        dt = datetime.now(timezone.utc)
        eth_gas_oracle_data = eth_gas_oracle(last_block = result['LastBlock'],
                                    safe_gas_price =  result['SafeGasPrice'],
                                    propose_gas_price = result['ProposeGasPrice'],
                                    fast_gas_price = result['FastGasPrice'],
                                    update_id = 'pawethgasoracle',
                                    update_tmstmp = dt
                                    )

        #load data to db eth_gas_oracle table
        with db_session() as s:
            #check if data is present in the table for last block id if preset skip if not add new record
            gas_oracle_indb = s.query(eth_gas_oracle).filter(eth_gas_oracle.last_block == result['LastBlock']).first()
            if not gas_oracle_indb:
                s.add(eth_gas_oracle_data)
    except Exception as e:
        logging.error("Insert data into eth_gas_oracle table failed! " + str(e))
        raise Exception(e)

if __name__ == '__main__':
    try:
        logging.info("----Read and Load ETH Oracle Data into gas----")
        
        eth_gas_oracle_result = read_eth_gas_oracle_api()
        load_eth_gas_oracle_db(eth_gas_oracle_result)

    except Exception as e:
        logging.error(traceback.print_exc())
        logging.error("Error in ETH Gas Oracle api processing .Please check! " + str(e))
        raise Exception(e)
        
