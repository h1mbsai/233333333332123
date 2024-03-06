import sqlite3 as sq

db = sq.connect('core/db/tg.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER)")
    db.commit()

async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()

async def get_tg_id(user_id):
    user = cur.execute("SELECT tg_id FROM accounts WHERE tg_id == key".format(key=user_id)).fetchone()
    if user:
        return user[0]
    else:
        return None
    