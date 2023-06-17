"""Module for interacting with database"""

import sqlite3

from tgbot.misc.constants import DATABASE


class DbInteraction:
    """Simple db interation class using sqlite."""

    def __init__(self, database):
        """Initialize connection and cursor."""
        self.connection = sqlite3.connect(database)
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
        """Check if user with current telegram id is in the database table 'user'."""
        sql_query = '''SELECT "user".id from "user" WHERE "user".id = (?)'''
        found_user = self.cur.execute(sql_query, (user_id,)).fetchone()
        if not found_user:
            return False
        return True

    def add_user_to_db(self, user_id, name, phone):
        """Add user to 'user' table."""
        sql_query = '''INSERT INTO "user" VALUES(?, ?, ?)'''
        self.cur.execute(sql_query, (user_id, name, phone))
        self.connection.commit()

    def get_username(self, user_id):
        """Fetch username by user id."""
        sql_query = '''SELECT username from "user" WHERE "user".id = (?)'''
        username = self.cur.execute(sql_query, (user_id,)).fetchone()[0]
        return username


db_interaction = DbInteraction(DATABASE)
