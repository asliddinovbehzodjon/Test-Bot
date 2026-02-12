import sqlite3
class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db, timeout=7)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
            data = cursor.lastrowid
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    # Create table
    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NULL ,
            name varchar(255) NULL,
            telegram_id varchar(20) UNIQUE,
            language varchar(3) NULL,
            role varchar(255) NULL,
            guruh varchar(250) NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int = None, name: str = None, telegram_id: str = None, language: str = 'uz',role:str=None,guruh:str=None):
        try:
            sql = """
        INSERT INTO Users(id, name,telegram_id, language,role,guruh) VALUES(?, ?, ?, ?,?,?)
        """
            return self.execute(sql, parameters=(id, name, telegram_id, language,role,guruh), commit=True)
        except:
            self.connection.close()

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        all_users = []
        data = self.execute(sql, fetchall=True)
        for i in data:
            all_users.append({
                'id': i[0],
                'name': i[1],
                'telegram_id': i[2],
                'language': i[3],
                'role': i[4],
                'guruh': i[5]
             
            })
        return all_users

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        i = self.execute(sql, parameters=parameters, fetchone=True)
        if i:
            user_info = {
                'id': i[0],
                'name': i[1],
                'telegram_id': i[2],
                'language': i[3],
                'role': i[4],
                'guruh': i[5]
            }
            return user_info
        else:
            return {}

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_language(self, language, telegram_id):

        sql = f"""
        UPDATE Users SET language=? WHERE telegram_id=?
        """
        return self.execute(sql, parameters=(language, telegram_id), commit=True)
    def update_user_name(self, name, telegram_id):

        sql = f"""
        UPDATE Users SET name=? WHERE telegram_id=?
        """
        return self.execute(sql, parameters=(name, telegram_id), commit=True)
    def update_user_role(self, role, telegram_id):

        sql = f"""
        UPDATE Users SET role=? WHERE telegram_id=?
        """
        return self.execute(sql, parameters=(role, telegram_id), commit=True)
    def update_user_group(self, guruh, telegram_id):

        sql = f"""
        UPDATE Users SET guruh=? WHERE telegram_id=?
        
        """
        return self.execute(sql, parameters=(guruh, telegram_id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
#  Create table test  answers
    def create_table_answers(self):
        sql = """
        CREATE TABLE Answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code varchar(250) NULL UNIQUE,
            answers varchar(250) NULL,
            type_test varchar(250) NULL,
            telegram_id varchar(250)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_test(self, code: int = None, answers: str = None,type_test:str=None,telegram_id:str=None):
        try:
            sql = """
        INSERT INTO Answers(code,answers,type_test,telegram_id) VALUES(?,?,?,?)
        """
            data = self.execute(sql, parameters=(code, answers,type_test,telegram_id), commit=True)
            return data
        except:
            self.connection.close()

 
    def select_test(self, **kwargs):
        sql = "SELECT * FROM Answers WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        i = self.execute(sql, parameters=parameters, fetchone=True)
        if i:
            channel_info = {
                'code': i[0],
                'answers': i[2],
                'type_test': i[3],
                'telegram_id': i[4]
            }
            return channel_info
        else:
            return {}

    def delete_answers(self,id):
        sql = f"""
        DELETE FROM Answers WHERE id=?
        """
        return self.execute(sql, parameters=(id,), commit=True)
    # Create Channel Table
    def create_table_channels(self):
        sql = """
        CREATE TABLE Channels(
            id int NULL ,
            channel_name varchar(255) NULL,
            channel_id varchar(255) UNIQUE,
            channel_members_count varchar(255) NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_channel(self, id: int = None, channel_name: str = None, channel_id: str = None,
                    channel_members_count: str = None):
        try:
            sql = """
        INSERT INTO Channels(id, channel_name,channel_id, channel_members_count) VALUES(?, ?, ?, ?)
        """
            return self.execute(sql, parameters=(id, channel_name, channel_id, channel_members_count), commit=True)
        except:
            self.connection.close()

    def select_all_channels(self):
        sql = """
        SELECT * FROM Channels
        """
        all_channels = []
        data = self.execute(sql, fetchall=True)
        if data:
            for i in data:
                all_channels.append({
                    'id': i[0],
                    'channel_name': i[1],
                    'channel_id': i[2],
                    'channel_members_count': i[3]
                })
            return all_channels
        else:
            return all_channels

    def select_channel(self, **kwargs):
        sql = "SELECT * FROM Channels WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        i = self.execute(sql, parameters=parameters, fetchone=True)
        if i:
            channel_info = {
                'id': i[0],
                'channel_name': i[1],
                'channel_id': i[2],
                'channel_members_count': i[3]
            }
            return channel_info
        else:
            return {}

    def count_channels(self):
        return self.execute("SELECT COUNT(*) FROM Channels;", fetchone=True)

    def delete_channel(self, channel_id):
        sql = f"""
        DELETE FROM Channels WHERE channel_id=?
        """
        return self.execute(sql, parameters=(channel_id,), commit=True)

#  Create table test  Results
    def create_table_results(self):
        sql = """
        CREATE TABLE Results (
            code varchar(250) NULL,
            name varchar(250) NULL,
            trues varchar(250) NULL,
            falses varchar(250) NULL,
            telegram_id varchar(250)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_result(self, code: int = None, name: str = None,trues:str=None,falses:str=None,telegram_id:str=None):
        try:
            sql = """
        INSERT INTO Results(code,name,trues,falses,telegram_id) VALUES(?,?,?,?,?)
        """
            return (self.execute(sql, parameters=(code,name,trues,falses,telegram_id), commit=True))
        except:
            self.connection.close()

 
    def select_all_results(self,**kwargs):
        sql = "SELECT * FROM Results WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        
        all_results = []
        data = self.execute(sql, parameters=parameters,fetchall=True)
        if data:
            for i in data:
                all_results.append({
                    'code': i[0],
                    'name': i[1],
                    'trues': i[2],
                    'falses': i[3],
                    'telegram_id': i[4]
                })
            return all_results
        else:
            return all_results
    def select_result(self, **kwargs):
        try:
            sql = "SELECT * FROM Results WHERE "
            sql, parameters = self.format_args(sql, kwargs)
            i = self.execute(sql, parameters=parameters, fetchone=True)
            if i:
                result_info = {
                    'code': i[0],
                    'name': i[1],
                    'trues': i[2],
                    'falses':i[3],
                    'telegram_id':int(i[4])
                   
                }
                return result_info
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
    def delete_result(self,code):
        sql = f"""
        DELETE FROM Results WHERE code=?
        """
        return self.execute(sql, parameters=(code,), commit=True)
        