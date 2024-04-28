from dbutils.pooled_db import PooledDB
import pyodbc

# Database connection parameters

server = 'DESKTOP-M1K1OIB'
database = 'lms5'

driver = 'SQL SERVER'
trusted_connection = 'yes'
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}"

# Create a connection pool
pool = PooledDB(
    creator=pyodbc,
    mincached=1,
    maxcached=5,
    maxconnections=10,
    blocking=True,
    host=server,
    database=database,
    driver=driver
)

# Global variable to hold the shared connection
shared_connection = None

# Function to initialize and get the shared connection
def get_shared_connection():
    global shared_connection
    if shared_connection is None:
        shared_connection = pool.connection()
    return shared_connection
