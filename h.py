import sqlite3 as sql




con = sql.connect("Trainsss.db")

cur = con.cursor()

user = "bob"

hello = cur.execute(f'''SELECT * FROM BillettKjoep
            INNER JOIN SeteBillett ON BillettKjoep.BestillingsID = SeteBillett.BestillingsID
            INNER JOIN TogruteForekomst ON Billett.TogruteForekomstID = TogruteForekomst.TogruteForekomsID
            WHERE BillettKjoep.KjoeptAv = {user}''')

print(hello)

