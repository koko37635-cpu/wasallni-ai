import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    _instance = None
    _pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._pool is None:
            self._pool = psycopg2.pool.SimpleConnectionPool(
                1,
                20,
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT", 5432)
            )

    def get_connection(self):
        return self._pool.getconn()

    def put_connection(self, conn):
        self._pool.putconn(conn)

    def close_all(self):
        self._pool.closeall()

db = Database()
