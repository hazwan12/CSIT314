import sqlite3
import datetime

class Model(object):
    table_name = ""
    def __init__(self):
        self.conn = sqlite3.connect("bugzilla.db")

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
    table_name = "user"
    def __init__(self):
        super().__init__()

    def gen_insert(self, email : str, full_name : str, phone_no : str, password : str, created_dt : str = str(datetime.datetime.now())):
        return """
        INSERT INTO {} (email, full_name, phone_no, password, created_dt) 
        VALUES ({}, {}, {}, {}, {})
        """.format(self.table_name, email, full_name, phone_no, password, created_dt)

    def check_login(self, email : str, password : str):
        cursor = self.conn.cursor()
        cursor.execute("select count(*) from user where email = '{}' and password = '{}'".format(email, password))
        result = cursor.fetchall()

        if result[0][0] == 1:
            return True
        else:
            return False

class Bug(Model):
    table_name = "bug"
    def __init__(self):
        super().__init__()

    def gen_insert(self, reporter : str, title : str, description : str, created_dt : str = str(datetime.datetime.now())):
        return """
        INSERT INTO {} (reporter, title, description, created_dt) 
        VALUES ({}, {}, {}, {})
        """.format(self.table_name, reporter, title, description, created_dt)
