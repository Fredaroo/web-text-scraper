# coding: utf-8
import sqlite3
import csv

# connecting to the db and checking whether db exists: if not creates one (initiate_connection function)
conn = sqlite3.connect('url_data.db')


def initiate_connection():
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             uuid INTEGER,
             url TEXT,
             content TEXT
        )
        """)
        conn.commit()
    except sqlite3.OperationalError:
        print("[ERROR] Connection not initiated - terminate script")
        conn.close()


def import_data(file_name):
    try:
        cursor = conn.cursor()
        with open(file_name, 'r') as fin:
            # csv.DictReader uses first line in file for column headings
            dr = csv.DictReader(fin)  # comma is default delimiter
            try:
                to_db = [(i['uuid'], i['url']) for i in dr]
            except KeyError:
                print("[ERROR] The csv you provided does not follow the format guidelines")
                conn.close()
        cursor.executemany("INSERT INTO urls (uuid, url) VALUES (?, ?);", to_db)
        conn.commit()
        print("[OK] data loaded successfully")
    except sqlite3.Error:
        print("[ERROR] There was an error importing your data - terminate script")
        conn.close()


def get_length():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id) FROM urls;")
    data_size = cursor.fetchone()
    return data_size[0]


def get_url(id_value):
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM urls WHERE id = ?", (id_value,))
    fetched_url = cursor.fetchone()
    return fetched_url[0]


def get_last_range():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM urls WHERE content IS NOT NULL;")
    fetched_length = cursor.fetchone()
    return fetched_length[0]


def upload_content(url_content, i):
    cursor = conn.cursor()
    cursor.execute("UPDATE urls SET content = ? WHERE id = ?", (url_content, i))
    conn.commit()
    print("[OK] Reached --- uploaded Nb :" + str(i))
