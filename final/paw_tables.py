from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date,create_engine, Numeric,DateTime

Base = declarative_base()

class eth_price(Base):
    __tablename__ = 'eth_price'

    id = Column('id',Integer, primary_key=True)
    eth_btc = Column('eth_btc',Numeric(20,10))
    eth_btc_tmstmp = Column('eth_btc_tmstmp',Numeric)
    eth_usd = Column('eth_usd',Numeric(20,10))
    eth_usd_tmstmp  = Column('eth_usd_tmstmp',Numeric)    
    update_id = Column('update_id',String(20))
    update_tmstmp = Column('update_tmstmp',DateTime)
    
class eth_gas_oracle(Base):
    __tablename__ = 'eth_gas_oracle'

    id = Column('id', Integer,primary_key=True)
    last_block = Column('last_block',Numeric,index=True,unique=True)
    safe_gas_price = Column('safe_gas_price',Numeric)
    propose_gas_price = Column('propose_gas_price',Numeric)
    fast_gas_price = Column('fast_gas_price',Numeric)
    update_id = Column('update_id',String(20))
    update_tmstmp = Column('update_tmstmp',DateTime)

class eth_block_uncle_reward(Base):
    __tablename__ = 'eth_block_uncle_reward' 

    block_num =  Column('block_num',Integer,primary_key = True)   
    seq_id    = Column('seq_id',Integer,primary_key = True)
    block_tmstmp = Column('block_tmstmp',Numeric)
    block_miner = Column('block_miner',String(400))
    block_reward = Column('block_reward',Numeric)
    uncles_miner = Column('uncles_miner',String(400))
    uncles_postition = Column('uncles_postition',Numeric)
    uncles_block_reward = Column('uncles_block_reward',Numeric)
    uncle_inclusion_reward = Column('uncle_inclusion_reward',Numeric)
    update_id =  Column('update_id',String(20))
    update_tmstmp = Column('update_tmstmp',DateTime)

