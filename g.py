import sqlite3 as sql
from d import finneTogruter


con = sql.connect("Trainsss.db")
cur = con.cursor()


for rute in cur.execute(f'''SELECT * FROM Togrute''').fetchall():
    print(rute)

startstasjon = input("Hvor reiser du fra?")
endestasjon = input("Hvor skal du?")
dato = input("Hvilken dato reiser du")
klokkeslett = input("Når????????????")

finneTogruter(startstasjon, endestasjon, dato, klokkeslett)

rute = int(input("Hvilken rute vil du ta?: "))