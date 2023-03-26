import sqlite3 as tissefant
import sys

def finn_ruter_gjennom_stasjon():

    dag = input("Hvilken dag vil du se: ").lower()

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
    else:
        finn_ruter_gjennom_stasjon()
        exit()

    stasjon = input("Stasjon: (hust stor forbokstav)")
    stasjon = '"' + stasjon + '"'

    con = tissefant.connect("Trainsss.db")

    cur = con.cursor()


    query = f'''SELECT * FROM Togrute 
    INNER JOIN TogruteBesoekerStasjon ON Togrute.TogruteID = TogruteBesoekerStasjon.TogruteID 
    WHERE Togrute.dager LIKE "{dag}" AND TogruteBesoekerStasjon.StasjonNavn = {stasjon}'''

    res = cur.execute(query).fetchall()
    for i in range(len(res)):
        print(f"Rute: {res[i][0]} \n \nOperatør: {res[i][3]}\nAnkomst: {res[i][6]} \nAvreise: {res[i][7]}")
