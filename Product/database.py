import psycopg2

"""
    To get started, execute the following SQL on the Postgres server:
        create database uis;
        create user uis with password 'uis';
        grant all privileges on database uis to uis;
        grant all privileges on all tables in schema public to uis;
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to uis;
"""

connection = psycopg2.connect(
    database='uis',
    user='uis',
    host='localhost',
    password='uis'
);

def execute(query):
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    return cur
