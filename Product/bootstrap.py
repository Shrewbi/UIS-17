import database

def create_tables():
    database.execute("""
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
          name VARCHAR(255) NOT NULL
        );

        CREATE TABLE template_fields(
          id SERIAL PRIMARY KEY,
          name VARCHAR(255) NOT NULL,
          template_id INT REFERENCES templates(id),
          media_id INT REFERENCES media(id) ON DELETE CASCADE
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
          item_id INT REFERENCES items(id) ON DELETE CASCADE,
          media_id INT REFERENCES media(id) ON DELETE CASCADE
        );

        CREATE TABLE paths(
          from_item_id INT REFERENCES items(id) ON DELETE CASCADE,
          to_item_id INT REFERENCES items(id) ON DELETE CASCADE
        );
    """)

def add_constraints_and_triggers():
    database.execute("""
        CREATE OR REPLACE FUNCTION check_media_type()
        RETURNS TRIGGER AS
        $$
        BEGIN
          NEW.type := lower(NEW.type);
          IF NEW.type NOT IN ('text', 'image', 'video') THEN
            RAISE EXCEPTION 'Invalid item type, valid types are: "text", "image", or "video"';
          END IF;
          RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER check_media_type_trigger
        BEFORE INSERT OR UPDATE ON media
        FOR EACH ROW EXECUTE PROCEDURE check_media_type();
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
add_constraints_and_triggers()
