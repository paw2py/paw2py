from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json
import requests
from datetime import datetime
import time
from pytz import timezone
import logging
import traceback
from config import *
from paw_tables import *
from paw_eth_stats_crud import db_session



set_logger(logging)
est_tz = timezone('EST')


def get_unix_time():
    dtnow = datetime.now(est_tz)
    return int(time.mktime(dtnow.timetuple()))


def read_block_num(unxtm):
    try:
        
        url = eth_block_by_unxtmstmp + str(unxtm) + eht_block_2nd
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()['result']
        else:
            raise Exception("ETH Block Number API status code != 200 " + str(r.starue_code))
    except Exception as e:
        logging.error("There is issue with ETH Block Number url! " + str(e))
        raise Exception(e)    



def read_eth_block_uncle_reward_api(blk_number):
    try:
        logging.info("----get ETH Block Uncle Rewar from get block and uncle  API [pass block number]----")
        #read block uncle reward api
        url_block_uncle = eth_block_uncle_reward_api + str(blk_number) + eht_block_uncle_2nd       
        r = requests.get(url_block_uncle)
        if r.status_code == 200:
            return r.json()['result']
        else:
            raise Exception("ETH Block Uncle Reward API stats code != 200 " + str(r.starue_code))
    except Exception as e:
        logging.error("There is issue with ETH Block Uncle Reward url! " + str(e)) 
        raise Exception(e)
 
def load_eth_block_uncle_reward_db(result):
    try:
        logging.info("----Load ETH Block Uncle Reward  to eth_block_uncle_reward table----")
        dt = datetime.now(est_tz)
        if result['uncles']:
            #response from api has nested uncles
            uncles = 1
            eth_blk_uncl_rwd_data = ([eth_block_uncle_reward(block_num = result['blockNumber'],
                                    seq_id =  idx+1,
                                    block_tmstmp = result['timeStamp'],
                                    block_miner = result['blockMiner'],
                                    block_reward = result['blockReward'],
                                    uncles_miner = val['miner'],
                                    uncles_postition = val['unclePosition'],
                                    uncles_block_reward = val['blockreward'],
                                    uncle_inclusion_reward = result['uncleInclusionReward'] ,                                   
                                    update_id = 'pawethblkunclrwd',
                                    update_tmstmp = dt)
                                    for idx, val in enumerate(result['uncles'])
                                    ])
        else:
            # the response from api dose not have any nested uncles
            uncles = 0 
            eth_blk_uncl_rwd_data = eth_block_uncle_reward(block_num = result['blockNumber'],
                                    seq_id =  1,
                                    block_tmstmp = result['timeStamp'],
                                    block_miner = result['blockMiner'],
                                    block_reward = result['blockReward'],
                                    uncle_inclusion_reward = result['uncleInclusionReward'] ,                                   
                                    update_id = 'pawethblkunclrwd',
                                    update_tmstmp = dt
                                    )
            #load data to db eth_block_uncle_reward table
        with db_session() as s:
            if uncles == 1:
                s.add_all(eth_blk_uncl_rwd_data)
            else:
                s.add(eth_blk_uncl_rwd_data)    
    except Exception as e:
        logging.error("Insert data into eth_block_uncle_reward table failed! " + str(e))
        raise Exception(e)

if __name__ == '__main__':
    try:
        logging.info("----Read and Load ETH Block Uncle Rewards  Data into eth_block_uncle_reward----")
        
        #get time in unix number
        unxtime = get_unix_time()
        logging.info('unx time ' + str(unxtime))

        #get block number 
        blk_num = read_block_num(unxtime)
        logging.info('block number ' + str(blk_num))

        #call block uncle reward using block number
        eth_blk_uncl_rwd_result = read_eth_block_uncle_reward_api(blk_num)
        
        load_eth_block_uncle_reward_db(eth_blk_uncl_rwd_result)

    except Exception as e:
        logging.error(traceback.print_exc())
        logging.error("Error in ETH Block Uncle Reward api processing .Please check! " + str(e))
        raise Exception(e)
        
