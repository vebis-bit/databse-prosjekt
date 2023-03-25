import sys
import sqlite3 as sql
import datetime as dt

startStasjon = sys.argv[1]

endeStasjon = sys.argv[2]

dato = sys.argv[3]
dtDato = dt.datetime.strptime(dato, "%d%m%Y").date()
weekday = dtDato.weekday()
weekdayMap = ["11_____", "_11____", "__11___", "___11__", "____11_", "_____11", "1_____1"]
weekdayString = weekdayMap[weekday]

con = sql.connect("Trainsss.db")
cur = con.cursor()

klokkeslett = sys.argv[4]


hovedretning = f'''SELECT StasjonNavn FROM BanestrekningHarStasjon 
WHERE StasjonNavn = "{startStasjon}" OR StasjonNavn = "{endeStasjon}"
ORDER BY Posisjon'''

a = cur.execute(hovedretning)

hovedRetning = a.fetchone()[0] == startStasjon


query = f'''SELECT * FROM Togrute
WHERE "{startStasjon}" IN (SELECT StasjonNavn FROM TogruteBesoekerStasjon INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID)
AND "{endeStasjon}" IN (SELECT StasjonNavn FROM TogruteBesoekerStasjon INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID)
AND Togrute.Dager LIKE "{weekdayString}"
AND Togrute.HovedRetning = {hovedRetning}
'''

b = cur.execute(query)

print(b.fetchall())