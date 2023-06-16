import sqlite3


class DbInteraction:
    def __init__(self):
        self.connection = sqlite3.connect("lifecell_db.db")
        self.cur = self.connection.cursor()

    def create_user_table(self):
        """Create table for user's in Telegram"""
        create_user_table_query = '''
            CREATE TABLE IF NOT EXISTS "user"(
            id BIGINT NOT NULL UNIQUE,
            username TEXT NOT NULL,
            phone TEXT NOT NULL
            )
        '''
        self.cur.execute(create_user_table_query)

    def check_user_in_db(self, user_id):
        sql_query = '''SELECT "user".id from "user" WHERE "user".id = (?)'''
        found_user = self.cur.execute(sql_query, (user_id,)).fetchone()
        if not found_user:
            return False
        return True

    def add_user_to_db(self, user_id, name, phone):
        sql_query = '''INSERT INTO "user" VALUES(?, ?, ?)'''
        self.cur.execute(sql_query, (user_id, name, phone))
        self.connection.commit()


db_interaction = DbInteraction()
