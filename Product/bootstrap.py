import database

def create_tables():
    database.execute("""
        CREATE TABLE test(
            id SERIAL,
            body VARCHAR
        );

        CREATE TABLE admins(
          id SERIAL PRIMARY KEY,
          username VARCHAR(255),
          password_hash VARCHAR(512)
        );

        CREATE TABLE media(
          id SERIAL PRIMARY KEY,
          type VARCHAR(10) NOT NULL,
          value VARCHAR(255)
        );

        CREATE TABLE templates(
          id SERIAL PRIMARY KEY,
          name VARCHAR(255) NOT NULL,
          creator_admin_id INT REFERENCES admins(id)
        );

        CREATE TABLE template_fields(
          id SERIAL PRIMARY KEY,
          name VARCHAR(255) NOT NULL,
          shared BOOLEAN NOT NULL,
          shared_media_id INT REFERENCES media(id) ON DELETE CASCADE
        );

        CREATE TABLE items(
          id SERIAL PRIMARY KEY,
          template_id INT REFERENCES templates(id) ON DELETE CASCADE,
          x_coordinate DOUBLE PRECISION NOT NULL,
          y_coordinate DOUBLE PRECISION NOT NULL
        );

        CREATE TABLE item_fields(
          id SERIAL PRIMARY KEY,
          name VARCHAR(255) NOT NULL,
          media_id INT REFERENCES media(id) ON DELETE CASCADE
        );

        CREATE TABLE paths(
          from_item_id INT REFERENCES items(id) ON DELETE CASCADE,
          to_item_id INT REFERENCES items(id) ON DELETE CASCADE
        );
    """)

def insert_testdata():
    database.execute("""
        insert into test(body) values ('Hello World');
        insert into test(body) values ('Foo');
        insert into test(body) values ('Bar');
    """)

def wipe():
    database.execute("""
        DROP TABLE IF EXISTS test;
        DROP TABLE IF EXISTS templates CASCADE;
        DROP TABLE IF EXISTS template_fields CASCADE;
        DROP TABLE IF EXISTS items CASCADE;
        DROP TABLE IF EXISTS item_fields CASCADE;
        DROP TABLE IF EXISTS paths CASCADE;
        DROP TABLE IF EXISTS media;
        DROP TABLE IF EXISTS admins;
    """)

# First time, run:
wipe()
create_tables()
insert_testdata()
