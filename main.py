import sqlite3 as sql
from d import finnTogruter
from c import finn_ruter_gjennom_stasjon
from e import registrer
from g import kjop_billett
from h import vis_fremtidige_reiser

mail = ""
telefonnummer = ""
fornavn = ""
etternavn = ""

con = sql.connect("Trainsss.db")
cur = con.cursor()

while True:
    brukerinput = input("Velkomment til togdatabasen \nEr du ny bruker tast 1 for å registrere deg\nEr du returnerende bruker, tast 2:\n")
    if brukerinput == "1":
        mail = input("Mail:")
        telfonnummer = input("Telfonnummer:")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn")
        registrer(fornavn, etternavn, mail, telefonnummer)
        break
    elif brukerinput == "2":
        while True:
            #try: 
            brukerinput = input("Hva er mailen din: ")
            mail = cur.execute(f'SELECT Email FROM Kunde WHERE Kunde.Email = "{brukerinput}"').fetchone()[0]
            telefonnummer = cur.execute(f'SELECT Telefonnummer FROM Kunde WHERE Kunde.Email = "{mail}"').fetchone()[0]
            fornavn = cur.execute(f'SELECT Fornavn FROM Kunde WHERE Kunde.Email = "{mail}"').fetchone()[0]
            break
            #except:
                #pass
        break

while True: 
    brukerinput = input(f"""Hei {fornavn}, Tast nummer for å bestemme handling: \n
    1: Finn ruter som går gjennom stasjon på gitt dag og neste\n
    2: Søk etter togruter mellom stasjoner\n
    3: Kjøp billett \n
    4: Vis fremtidige reiser \n
    5: Avslutt program \n
    """)
    if brukerinput == "1":
        finn_ruter_gjennom_stasjon()
    elif brukerinput == "2":
        stasjon1 = input("Hvilke Stasjon reiser du fra: ")
        stasjon2 = input("Hvor vil du reise til: ")
        dato = input("Hvilken dato (format ddmmyyyy)")
        klokkeslett = input("Klokkeslett: ")
        liste = finnTogruter(stasjon1, stasjon2, dato, klokkeslett)
        print(f'Avreisestasjon: {stasjon1} Ankomststasjon: {stasjon2}')
        for e in liste:
            print("Dag: ",e[0],"Toglinje: ", e[1],"Avgang: ", e[2],"Ankomst: ", e[3])
        input("Trykk enter for å gå videre")
    elif brukerinput == "3": 
        kjop_billett(mail)
    elif brukerinput == "4":
        vis_fremtidige_reiser(mail)
    elif brukerinput == "5":
        break

    
        
        

