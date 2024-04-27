from dbutils.pooled_db import PooledDB
import pyodbc

def connect():
    server = 'DESKTOP-M1K1OIB'
    database = 'lms3'
    driver = 'SQL SERVER'
    trusted_connection = 'yes'
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}"

    # Decrease the pool size and connections
    pool = PooledDB(
        pyodbc,
        mincached=1,   # Set mincached to 1 to keep at least one connection in the pool
        maxcached=2,   # Set maxcached to 5 to limit the maximum number of cached connections
        maxconnections=5,  # Set maxconnections to 10 to limit the maximum total connections in the pool
        blocking=True,
        host=server,
        database=database,
        driver=driver
    )

    return pool.connection()
