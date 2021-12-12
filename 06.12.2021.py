import sqlite3

if __name__:
    list = [9, "привет", 5, 7, 2, "дом", "мир", 10]
    db = sqlite3.connect("tabData.db")
    courser = db.cursor()
    courser.execute('''CREATE TABLE IF NOT EXISTS tabNumber
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            INTEGER)''')
    db.commit()
    courser.execute('''CREATE TABLE IF NOT EXISTS tabString
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    stroka TEXT)''')
    courser.execute('''DELETE FROM tabString''')
    db.commit()
    courser.execute('''DELETE FROM tabNumber''')
    db.commit()
    for item in list:
        if type(item) is int:
            if int(item) % 2 == 0:
                courser.execute('''INSERT INTO tabNumber(number)
                        VALUES (?)''', (int(item),))
                db.commit()
            else:
                courser.execute('''INSERT INTO tabString(stroka)
                                        VALUES (?)''', ("нечетное",))
                db.commit()
        else:
            courser.execute('''INSERT INTO tabString(stroka)
                                                    VALUES (?)''', (item,))
            db.commit()
            courser.execute('''INSERT INTO tabNumber(number)
                                    VALUES (?)''', (len(item),))
            db.commit()
    courser.execute('''SELECT number FROM tabNumber''')
    b = courser.fetchall()
    print(b, len(b))
    courser.execute('''SELECT stroka FROM tabString''')
    a = courser.fetchall()
    print(a, len(a))
    if len(b) > 5:
        courser.execute('''DELETE FROM tabString WHERE id = 1''')
        db.commit()
        courser.execute('''SELECT stroka FROM tabString''')
        a = courser.fetchall()
        print(a)
    else:
        courser.execute('''UPDATE tabString SET stroka = "hello" WHERE id = 1''')
        db.commit()
        courser.execute('''SELECT stroka FROM tabString''')
        a = courser.fetchall()
        print(a)