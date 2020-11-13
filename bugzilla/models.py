import sqlite3
import datetime

class Model(object):

    def __init__(self, table_name : str):
        self.conn = sqlite3.connect("bugzilla.db")
        self.table_name = table_name

    def gen_insert(self):
        return "INSERT INTO {} () VALUES ()".format(self.table_name)

    def gen_select(self):
        return "SELECT * FROM {}".format(self.table_name)

    def insert(self):
        try:
            self.conn.execute(self.gen_insert())
        except Exception as e:
            print(e)

    def to_string(self):
        try:
            result = self.conn.execute(self.gen_select())
        except Exception as e:
            print(e)
        else:
            return result

class User(Model):
    
    def __init__(self, table_name : str):
        super().__init__(table_name)

    def gen_insert(self, email : str, full_name : str, phone_no : str, password : str, created_dt : str = str(datetime.datetime.now())):
        return """
        INSERT INTO {} (email, full_name, phone_no, password, created_dt) 
        VALUES ({}, {}, {}, {}, {})
        """.format(self.table_name, email, full_name, phone_no, password, created_dt)

class Bug(Model):
    
    def __init__(self, table_name : str):
        super().__init__(table_name)

    def gen_insert(self, reporter : str, title : str, description : str, created_dt : str = str(datetime.datetime.now())):
        return """
        INSERT INTO {} (reporter, title, description, created_dt) 
        VALUES ({}, {}, {}, {})
        """.format(self.table_name, reporter, title, description, created_dt)
