import pymysql
import os

class Database:
    def __init__(self):
        # self.conn = sqlite3.connect('database.db')
        self.conn = pymysql.connect(
            host=os.getenv('DB_HOST'), 
            user=os.getenv('DB_USERNAME'), 
            password=os.getenv('DB_PASSWORD'), 
            database=os.getenv('DB_DATABASE')
            )
        self.cursor = self.conn.cursor()
        
    def first(self, query:str, params:tuple = None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchone()
        
    def all(self, query:str, params:tuple = None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def commit(self, query:str, params:tuple = None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        