import base64

DATABASE_URI = 'postgres+psycopg2://postgres:paw2py@localhost:5432/postgres'


eth_stats_price = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=UKHKYVJRYGYE6HC3K6NJT32CRPPUVV7VYH'

eth_gas_oracle_api = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=UKHKYVJRYGYE6HC3K6NJT32CRPPUVV7VYH'

eth_block_by_unxtmstmp = 'https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp='
eht_block_2nd = '&closest=before&apikey=UKHKYVJRYGYE6HC3K6NJT32CRPPUVV7VYH'

eth_block_uncle_reward_api = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno='
eht_block_uncle_2nd = '&apikey=UKHKYVJRYGYE6HC3K6NJT32CRPPUVV7VYH'


#db details:
host = 'localhost'
database = 'postgres'
user = 'postgres'
password = 'paw2py'

def set_logger(logging):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)