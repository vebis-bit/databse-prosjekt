import sqlite3 as sql
from d import finnTogruter

mail = ""
telefonnummer = ""
fornavn = ""
etternavn = ""

con = sql.connect("Trainsss.db")
cur = con.cursor()

while True:
    brukerinput = input("Velkomment til togdatabasen \nEr du ny bruker tast 1 for å registrere deg\nEr du returnerende bruker, tast 2")
    if brukerinput == 1:
        mail = input("Mail:")
        telfonnummer = input("Telfonnummer:")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn")
        break
    elif brukerinput == 2:
        while True:
            brukerinput = input("Hva er mailen din")
            mail = cur.execute(f"SELECT Email FROM Kunde WHERE Kunde.Email = {mail}")
            telefonnummer = cur.execute(f"SELECT Telefonnummer FROM Kunde WHERE Kunde.Email = {mail}")
            fornavn = cur.execute(f"SELECT Fornavn FROM Kunde WHERE Kunde.Email = {mail}")
            break
        break

while True: 
    brukerinput = input(f"Hei {fornavn}, Tast nummer for å bestemme handling: 1: Finn ")
        

