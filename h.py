import sqlite3 as sql
from tabulate import tabulate



def vis_fremtidige_reiser(user):
    print(user)
    con = sql.connect("Trainsss.db")

    cur = con.cursor()

    hello = [("fra", "til", "dag", "måned", "år", "Togrute", "Sete/sengeNR", "Vogn")]
    hello = hello + cur.execute(f'''SELECT SeteBillett.PaastigningsStasjon, SeteBillett.AvstigningsStasjon, TogruteForekomst.Dag, TogruteForekomst.maaned, TogruteForekomst.aar, TogruteForekomst.TogruteID, SeteBillett.SeteNR, SeteBillett.VognID FROM BillettKjoep
                INNER JOIN SeteBillett ON BillettKjoep.BestillingsID = SeteBillett.BestillingsID
                INNER JOIN TogruteForekomst ON SeteBillett.TogruteForekomstID = TogruteForekomst.TogruteForekomstID
                WHERE BillettKjoep.KjoeptAv = "{user}"''').fetchall()
    hello = hello + cur.execute(f'''SELECT SengeBillett.PaastigningsStasjon, SengeBillett.AvstigningsStasjon, TogruteForekomst.Dag, TogruteForekomst.maaned, TogruteForekomst.aar, TogruteForekomst.TogruteID, SengeBillett.SengNR, SengeBillett.VognID FROM BillettKjoep
                INNER JOIN SengeBillett ON BillettKjoep.BestillingsID = SengeBillett.BestillingsID
                INNER JOIN TogruteForekomst ON SengeBillett.TogruteForekomstID = TogruteForekomst.TogruteForekomstID
                WHERE BillettKjoep.KjoeptAv = "{user}"''').fetchall()

    print(tabulate(hello))

