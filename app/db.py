from mysql.connector.pooling import MySQLConnectionPool
import os
from dotenv import load_dotenv

load_dotenv()

pool = MySQLConnectionPool(
    pool_name='main_pool',
    pool_size=10,
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT')),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE')
    )

def get_conn():
    conn = pool.get_connection()
    try:
        yield conn
    finally:
        conn.close()
        
def init_db(conn):
    cursor = conn.cursor()
    
    sql = '''
    CREATE TABLE IF NOT EXISTS weapons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        weapon_id VARCHAR(50),
        weapon_name VARCHAR(50),
        weapon_type VARCHAR(50),
        range_km INT,
        weight_kg FLOAT,
        manufacturer VARCHAR(50),
        origin_country VARCHAR(50),
        storage_location VARCHAR(50),
        year_estimated INT,
        level_risk VARCHAR(50)
        );'''

    cursor.execute(sql)
    
    conn.commit()
    
def insert_records():
    pass