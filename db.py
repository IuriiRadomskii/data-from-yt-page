import pymysql.cursors
import os


def connect_to_db(host='localhost', user='root', password='password', db='my_db', charset='utf8mb4'):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=db,
                           charset=charset,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def add_row_query(data: tuple):
    return f"INSERT INTO yt_pages (name, duration, likes, dislikes, views, publish_date) " \
           f"VALUES ('{data[0]}', {str(data[1])}, {data[2]}, {data[3]}, {data[4]}, '{data[5]}')"
