import sqlite3 as sql


class Database:
    
    # Подключение к бд
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

    async def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM User WHERE userID = (?)",
                                         (user_id,)).fetchmany(1)
            return True if len(result) != 0 else False
        
    async def add_user(self, user_id, login):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'User' ('userID', 'login', 'roleID') VALUES ((?), (?), (?))",
                                       (user_id, login, 2))

    async def update_userlogin(self, user_id, new_login):
        with self.connection:
            return self.cursor.execute(f"UPDATE User SET login = (?) WHERE userID = (?)",
                                       (new_login, user_id))

    async def get_userlogin(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT login FROM User WHERE userID = (?)",
                                       (user_id,)).fetchmany(1).pop(0)[0]


DB = Database("sqlite_db.db")
