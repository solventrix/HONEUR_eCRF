import os, psycopg2, bcrypt, logging


class UserDatabase():

    USER_QUERY = "SELECT password FROM webapi.sec_user WHERE login = %s"

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def check_password(self, username, password):
        if not username:
            logging.warning("Username is required!")
            return False
        if not password:
            logging.warning("Password is required!")
            return False
        hashed_password = self.get_hashed_user_password(username)
        if not hashed_password:
            logging.warning("User not found!")
            return False
        return bcrypt.checkpw(str.encode(password), str.encode(hashed_password))

    def get_hashed_user_password(self, username):
        connection = None
        db_cursor = None
        try:
            connection = self.get_user_db_connection()
            db_cursor = connection.cursor()
            db_cursor.execute(self.USER_QUERY, [username])
            return db_cursor.fetchone()[0]
        except (Exception, psycopg2.Error) as error:
            logging.error("Error selecting password from use table", error)
        finally:
            if db_cursor: db_cursor.close()
            if connection: connection.close()

    def get_user_db_connection(self):
        return psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database)
