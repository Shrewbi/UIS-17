import database
import hashlib

def credentials_valid(username, password):
    query = """
        select *
        from admins a
        where a.username = '{}'
        and   a.password_hash = '{}'
    """
    query = query.format(username, hash_password(password))
    cursor = database.execute(query)
    rows = cursor.fetchall()
    return len(rows) > 0

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
