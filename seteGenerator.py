import sqlite3 as sql


con = sql.connect("trainsss.db")

cur = con.cursor()


cur.execute(f'''DELETE FROM Sete''')
cur.execute(f'''DELETE FROM Kupe''')

# Joiner Vogner og vogntype for å få antallSeter per rad og antall rader
vogner = cur.execute(f'''SELECT * FROM Vogn
                  INNER JOIN VognType ON Vogn.Vogntype = Vogntype.navn AND Vogn.OperatoerNavn = VognType.OperatoerNavn''').fetchall()

for vogn in vogner:
    vognID = vogn[0]
    # Sjekker at vogn er sittevogn, ikke sovevogn
    if vogn[7] == 0:
        for i in range(vogn[5]*vogn[6]):
            cur.execute(f'''INSERT INTO Sete VALUES ({i+1}, {vognID})''')
    else:
        for i in range(vogn[7]):
            cur.execute(f'''INSERT INTO Kupe VALUES ({i+1}, {vognID})''')

con.commit()