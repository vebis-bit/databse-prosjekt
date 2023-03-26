import sqlite3 as sql
from d import finnTogruter


con = sql.connect("Trainsss.db")
cur = con.cursor()


startstasjon = "Trondheim"#input("Hvor reiser du fra?")
endestasjon = "Bodø"#input("Hvor skal du?")
dato = "03042023"# input("Hvilken dato reiser du (format: ddmmyyyy)")
dag = int(dato[0:2])
maaned = int(dato[2:4])
aar = int(dato[4:8])
print(f"dag: {dag}, maaned: {maaned}, år: {aar}")



klokkeslett = input("Når????????????")

print(finnTogruter(startstasjon, endestasjon, dato, klokkeslett))

rute = int(input("Hvilken rute vil du ta?: "))

def stasjonNr(stasjon, r):
    return cur.execute(f'''SELECT TogruteBesoekerStasjon.RekkefoelgeNr FROM TogruteBesoekerStasjon
    INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
    INNER JOIN TogruteForekomst ON TogruteForekomst.TogruteID = Togrute.TogruteID
    WHERE TogruteBesoekerStasjon.StasjonNavn = "{stasjon}"
    AND TogruteForekomst.TogruteforekomstID = {r}''').fetchall()[0][0]



startstasjonNr = stasjonNr(startstasjon, rute)

endestasjonNr = stasjonNr(endestasjon, rute)


print(startstasjonNr)



TogruteForekomstID = cur.execute(f'''SELECT TogruteForekomstID FROM TogruteForekomst
                                 WHERE TogruteForekomst.dag = {dag} 
                                 AND TogruteForekomst.maaned = {maaned}
                                 AND TogruteForekomst.aar = {aar}
                                 AND TogruteForekomst.TogruteID = {rute}''').fetchall()[0][0]
print(TogruteForekomstID)


# Finner ledige seter
cur.execute(f'''SELECT (Sete.SeteNR, Sete.VognID, TogruteForekomst.TogruteForekomstID) FROM Sete 
            INNER JOIN VognITogrute ON Sete.VognID = VognITogrute.VognID
            INNER JOIN Togrute ON Togrute.TogruteID = VognITogrute.TogruteID
            INNER JOIN TogruteForekomst ON Togrute.TogruteID = TogruteForekomst.TogruteID
            WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}
            NOT IN
                (
                SELECT (Sete.SeteNR, Sete.VognID, TogruteForekomst.TogruteForekomstID) FROM SeteBillett
                INNER JOIN Sete ON SeteBillett.SeteNr = Sete.SeteNr AND SeteBillett.VognID = Sete.VognID
                INNER JOIN TogruteForekomst ON SeteBillett.TogruteforekomstID = TogruteForekomst.TogruteForekomstID
                WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}
                AND (
                    SeteBillett.avstigningsStasjon < 
                    
                    )
            )''')