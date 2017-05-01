import database

def create_tables():
    database.execute("""
        create table test(id SERIAL, body VARCHAR);
    """)

def insert_testdata():
    database.execute("""
        insert into test(body) values ('Hello World');
        insert into test(body) values ('Foo');
        insert into test(body) values ('Bar');
    """)

def wipe():
    database.execute("""
        drop table test;
    """)

# First time, run:
wipe()
create_tables()
insert_testdata()
