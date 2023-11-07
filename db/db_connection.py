
# setup function for creating database & tables

import sqlite3

DB_FILE_PATH = "Online_Portfolio.db"


# get connection to db
def get_db_connection(db_path=DB_FILE_PATH):
    connection = sqlite3.connect(db_path)
    return connection


# create database & create tables
def create_database(db_path=DB_FILE_PATH):
    # create database
    connection = sqlite3.connect(db_path)

    # create tables
    create_tables(connection)


def create_tables(connection):
    create_insta_table(connection)
    create_git_table(connection)
    create_fb_table(connection)


def create_insta_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Insta(
        id TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL
        );
        """
    )
    connection.commit()


def create_git_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Git(
        id TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL
        );
        """
    )
    connection.commit()


def create_fb_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FaceBook(
        id TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL
        );
        """
    )
    connection.commit()

