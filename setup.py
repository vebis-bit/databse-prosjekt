import sqlite3 as sql;




con = sql.connect("Trains.db")

cur = con.cursor()
cur.execute('INSERT INTO Banestrekning VALUES ("NordlandsBanen")')
cur.execute('INSERT INTO Stasjon VALUES ("Bodø", 4.1)')
cur.execute('INSERT INTO Stasjon VALUES ("Fauske", 34.0)')
cur.execute('INSERT INTO Stasjon VALUES ("Mo i Rana", 3.5)')
cur.execute('INSERT INTO Stasjon VALUES ("Mosjøen", 6.8)')
cur.execute('INSERT INTO Stasjon VALUES ("Steinkjer", 3.6)')
cur.execute('INSERT INTO Stasjon VALUES ("Trondheim", 5.1)')
cur.execute('INSERT INTO DelStrekning VALUES ("Bodø", "Fauske", 60, false)')
cur.execute('INSERT INTO DelStrekning VALUES ("Fauske", "Mo i Rana", 170, false)')
cur.execute('INSERT INTO DelStrekning VALUES ("Mo i Rana", "Mosjøen", 90, false)')
cur.execute('INSERT INTO DelStrekning VALUES ("Mosjøen", "Steinkjer", 280, false)')
cur.execute('INSERT INTO DelStrekning VALUES ("Steinkjer", "Trondheim", 120, true)')
cur.execute('INSERT INTO operatoer VALUeS ("SJ")')
cur.execute('''INSERT INTO Vogn(OperatoerNavn, TogruteID, AntallRader, SeterPerRad, AntallKupeer, Rekkefoelgenr)
            VALUES ("SJ", null, 3, 4, null, null)''')
cur.execute('''INSERT INTO Togrute''')

con.commit()