# from .json_updater import flipkart, amazon, paytm, snapdeal, json_update
import sqlite3


# def create_table():
#     connection = sqlite3.connect("../db.sqlite3")
#     cursor = connection.cursor()
#     tables = cursor.execute("CREATE TABLE USER(USER_ID INT, JSON_FILE_PATH CHAR(200))")


def sqlite_insert():
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    rows = [(1, "../json_values/user_1.json")]
    tables = cursor.executemany("insert into user values (?, ?)", rows)
    connection.commit()


def check_for_user_id(user_id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    user_id = [(user_id)]
    val = cursor.execute("SELECT JSON_FILE_PATH FROM USER WHERE USER_ID=(?)", user_id)
    val = cursor.fetchone()
    # print(val)
    if val != None:
        return True, val
    else:
        return False
    # connection.close()


# create_table()
# insert()
print(check_for_user_id(1))
