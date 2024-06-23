import sqlite3 as sq

async def db1_start():
    global db, cur

    db = sq.connect('base2.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, Media TEXT, username TEXT, description TEXT)")
    
    db.commit()

async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?)", (user_id, '', '', ''))
        db.commit()

async def edit(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET Media = '{}', username = '{}', description = '{}' WHERE user_id == '{}'"
                    .format(data['Media'], data['username'], data['description'], user_id))
        db.commit()