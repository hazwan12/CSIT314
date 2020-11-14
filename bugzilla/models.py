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
        VALUES ('{}', '{}', '{}', '{}', '{}')
        """.format(self.table_name, email, full_name, phone_no, password, created_dt)

    def check_login(self, email : str, password : str):
        cursor = self.conn.cursor()

        #Check if user exists
        cursor.execute("select count(1) from user where email = '{}'".format(email))
        result = cursor.fetchall()

        if result[0][0] == 0:
            return False, "User {} does not exist. Please register".format(email)

        else:
            cursor.execute("select count(1) from user where email = '{}' and password = '{}'".format(email, password))
            result = cursor.fetchall()

            if result[0][0] == 0 :
                return False, "Error in credentials. Please try again"
            else:
                return True, "Login Suceeded, Welcome {}!".format(email)

    def registration(self, email : str, full_name : str, phone_no : str, password : str):
        cursor = self.conn.cursor()

        #Check if user exists
        cursor.execute("select count(1) from user where email = '{}'".format(email))
        result = cursor.fetchall()

        if result[0][0] == 1:
            return False, "User {} is already registered. Please login".format(email)
        else:
            try:
                cursor.execute(self.gen_insert(email, full_name, phone_no, password))
                self.conn.commit()
            except Exception as e:
                print(e)
                return False, "Error in user creation, please try again"
            else:
                return True, "Account created successfully, please proceed to login"
            
class Bug(Model):
    table_name = "bug"
    def __init__(self):
        super().__init__()

    def gen_insert(self, reporter : str, title : str, description : str, created_dt : str = str(datetime.datetime.now())):
        return """
        INSERT INTO {} (reporter, title, description, created_dt) 
        VALUES ({}, {}, {}, {})
        """.format(self.table_name, reporter, title, description, created_dt)

    def to_html_cards(self):

        def gen_card(row):
            reporter = row[1]
            title = row[2]
            description = row[3]
            created_dt = row[4]   
            return """
                <div class="card" style="width: 25rem;">
                    <div class="card-body">
                        <h5 class="card-title">{}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Reported By : {}</h6>
                        <h6 class="card-subtitle mb-2 text-muted">Reported On : {}</h6>
                        <p class="card-text">{}</p>
                        <a href="#" class="card-link">View Details</a>
                    </div>
                </div>
            """.format(title, reporter, created_dt, description)

        cursor = self.conn.cursor()
        cursor.execute("select * from bug")
        result = cursor.fetchall()
        
        i = 0
        bug_card_list = [] 
        for row in result:
            if i == 0:
                bug_card_list.append('<div class="card-deck">')
            bug_card_list.append(gen_card(row))
            i += 1

            if i == 3:
                bug_card_list.append("</div><br>")
                i=0

        return " ".join(bug_card_list)
