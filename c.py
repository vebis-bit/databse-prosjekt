import sqlite3 as tissefant
import sys

dag = sys.argv[2].lower()

if(dag == "mandag"):
    dag = "1______"
elif(dag == "tirsdag"):
    dag = "_1_____"
elif(dag == "onsdag"):
    dag = "__1____"
elif(dag == "torsdag"):
    dag = "___1___"
elif(dag == "fredag"):
    dag = "____1__"
elif(dag == "lørdag"):
    dag = "_____1_"
elif(dag == "søndag"):
    dag = "______1"

stasjon = sys.argv[1]
stasjon = '"' + stasjon + '"'

con = tissefant.connect("Trainsss.db")

cur = con.cursor()

query = f'''SELECT * FROM Togrute 
INNER JOIN TogruteBesoekerStasjon ON Togrute.TogruteID = TogruteBesoekerStasjon.TogruteID 
WHERE Togrute.dager LIKE "{dag}" AND TogruteBesoekerStasjon.StasjonNavn = {stasjon}'''

print(query)

res = cur.execute(query)

print(res.fetchall())
