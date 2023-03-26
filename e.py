import sqlite3 as tissefant
import sys

def registrer(fornavn, etternavn, email, telefonnr):
    con = tissefant.connect("Trainsss.db")
    cur = con.cursor()

    query = f'INSERT INTO Kunde(Fornavn, Etternavn, Email, TelefonNummer) VALUES("{fornavn}", "{etternavn}", "{email}", {telefonnr})'

    print(query)

    res = cur.execute(query)

    print(res.fetchall())

    con.commit()