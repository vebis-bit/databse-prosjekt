import sqlite3 as tissefant
import sys

fornavn = sys.argv[1]
etternavn = sys.argv[2]
email = sys.argv[3]
telefonnr = sys.argv[4]

con = tissefant.connect("Trainsss.db")
cur = con.cursor()

query = f'INSERT INTO Kunde(Fornavn, Etternavn, Email, TelefonNummer) VALUES("{fornavn}", "{etternavn}", "{email}", {telefonnr})'

print(query)

res = cur.execute(query)

print(res.fetchall())

con.commit()