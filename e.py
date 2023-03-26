import sqlite3 as sql
import sys

def registrer(fornavn, etternavn, email, telefonnr):
    con = sql.connect("Trainsss.db")
    cur = con.cursor()

    query = f'INSERT INTO Kunde(Fornavn, Etternavn, Email, TelefonNummer) VALUES("{fornavn}", "{etternavn}", "{email}", "{telefonnr}")'

    res = cur.execute(query)

    con.commit()