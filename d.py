import sys
import sqlite3 as sql
import datetime as dt

startStasjon = input("Hvor reiser du fra?")
endeStasjon = input("Hvor skal du?")
dato = input("Hvilken dato reiser du")
klokkeslett = input("Når????????????")

def finnTogruter(startStasjon, endeStasjon, dato, klokkeslett):
    dtDato = dt.datetime.strptime(dato, "%d%m%Y").date()
    weekday = dtDato.weekday()
    weekdayMap = ["1______", "_1_____", "__1____", "___1___", "____1__", "_____1_", "______1"]
    weekdayString = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
    day = weekdayMap[weekday]
    nextDay = weekdayMap[(weekday+1)%7]

    con = sql.connect("Trainsss.db")
    cur = con.cursor()

    hovedretning = f'''SELECT StasjonNavn FROM BanestrekningHarStasjon 
    WHERE StasjonNavn = "{startStasjon}" OR StasjonNavn = "{endeStasjon}"
    ORDER BY Posisjon'''

    a = cur.execute(hovedretning)

    hovedRetning = a.fetchone()[0] == startStasjon


    query = f'''SELECT * FROM Togrute
    WHERE "{startStasjon}" IN (SELECT StasjonNavn FROM TogruteBesoekerStasjon 
    INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID)
    AND "{endeStasjon}" IN (SELECT StasjonNavn FROM TogruteBesoekerStasjon 
    INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID)
    AND (Togrute.Dager LIKE "{day}"
    OR Togrute.Dager LIKE "{nextDay}")
    AND Togrute.HovedRetning = {hovedRetning}
    '''


    res = cur.execute(query).fetchall()

    table = []
    for entry in res:
        entry[0]

        avgangsTid = cur.execute(f'''SELECT Avgang FROM Togrute
        INNER JOIN TogruteBesoekerStasjon ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
        WHERE Togrute.TogruteID = {entry[0]}
        AND TogruteBesoekerStasjon.StasjonNavn = "{startStasjon}"''').fetchone()
        

        ankomstTid = cur.execute(f'''SELECT Ankomst FROM Togrute
        INNER JOIN TogruteBesoekerStasjon ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
        WHERE Togrute.TogruteID = {entry[0]}
        AND TogruteBesoekerStasjon.StasjonNavn = "{endeStasjon}"''').fetchone()

        
        try:
            cur.execute(f'''SELECT * FROM Togrute 
            INNER JOIN TogruteBesoekerStasjon ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
            WHERE Togrute.Dager LIKE "{day}"
            AND Togrute.TogruteID = {entry[0]}''').fetchall()[0]
            table.append((weekdayString[weekday], entry[0], avgangsTid[0], ankomstTid[0]))
        except(IndexError):
            pass
        try:
            cur.execute(f'''SELECT * FROM Togrute 
            INNER JOIN TogruteBesoekerStasjon ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
            WHERE Togrute.Dager LIKE "{nextDay}"
            AND Togrute.TogruteID = {entry[0]}''').fetchall()[0]
            table.append((weekdayString[(weekday+1)%7], entry[0], avgangsTid[0], ankomstTid[0]))
        except(IndexError):
            pass 
            
    liste = []
    for i in range(len(table)):
        if table[i][0] == weekdayString[weekday]:
            liste.append(table[i])

    for i in range(len(table)):
        if table[i][0] == weekdayString[(weekday+1)%7]:
            liste.append(table[i])



    print(liste)
finnTogruter(startStasjon, endeStasjon, dato, klokkeslett)