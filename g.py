import sqlite3 as sql
from d import finnTogruter

def kjop_billett(BrukerEmail):
    con = sql.connect("Trainsss.db")
    cur = con.cursor()



    startstasjon = input("Hvor reiser du fra?")
    endestasjon = input("Hvor skal du?")
    dato = input("Hvilken dato reiser du (format: ddmmyyyy)")
    dag = int(dato[0:2])
    maaned = int(dato[2:4])
    aar = int(dato[4:8])
    print(f"dag: {dag}, maaned: {maaned}, år: {aar}")



    klokkeslett = input("Klokkeslett: ")

    togruter = finnTogruter(startstasjon, endestasjon, dato, klokkeslett)
    for i in range(len(togruter)):
        togruter[i] = (togruter[i][1],togruter[i][2],togruter[i][3])
    togruter = list(dict.fromkeys(togruter))
    
    
    for rute in togruter:
        print(f"rute: {rute[0]} Avreisertidspunkt: {rute[1]} AnkomstTidspunkt: {rute[2]}")
        
    try: 
        rute = int(input("Hvilken rute vil du ta?: "))
    except:
        print("Støtte for valgt dato eksisterer ikke")

    def stasjonNr(stasjon, r):
        return cur.execute(f'''SELECT TogruteBesoekerStasjon.RekkefoelgeNr FROM TogruteBesoekerStasjon
        INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
        INNER JOIN TogruteForekomst ON TogruteForekomst.TogruteID = Togrute.TogruteID
        WHERE TogruteBesoekerStasjon.StasjonNavn = "{stasjon}"
        AND TogruteForekomst.TogruteforekomstID = {r}''').fetchall()[0][0]


    def stasjonerMellom(startNR, sluttNR, togruteForekomstID):
        return cur.execute(f'''SELECT Stasjon.Navn FROM TogruteBesoekerStasjon
        INNER JOIN Togrute ON TogruteBesoekerStasjon.TogruteID = Togrute.TogruteID
        INNER JOIN Stasjon ON TogruteBesoekerStasjon.StasjonNavn = Stasjon.Navn
        INNER JOIN TogruteForekomst ON TogruteForekomst.TogruteID = Togrute.TogruteID
        WHERE TogruteBesoekerStasjon.RekkefoelgeNr <= {sluttNR-1}
        AND TogruteBesoekerStasjon.RekkefoelgeNr >= {startNR}
        AND TogruteForekomst.TogruteforekomstID = {togruteForekomstID}''').fetchall()
        

    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return len(lst3) > 0

    # Finner togruteforekomster som stemmer overens med ønsket dato og strekning
    TogruteForekomstID = cur.execute(f'''SELECT TogruteForekomstID FROM TogruteForekomst
                                    WHERE TogruteForekomst.dag = {dag} 
                                    AND TogruteForekomst.maaned = {maaned}
                                    AND TogruteForekomst.aar = {aar}
                                    AND TogruteForekomst.TogruteID = {rute}''').fetchall()[0][0]


    startstasjonNr = stasjonNr(startstasjon, TogruteForekomstID)
    endestasjonNr = stasjonNr(endestasjon, TogruteForekomstID)





    print(TogruteForekomstID)

    # Finner eksisterenede billetter tilhørende ønsket togruteforekomst i databasen
    kjøpteSeteBilletter = cur.execute(f'''SELECT Sete.SeteNR, Sete.VognID, TogruteForekomst.TogruteForekomstID, SeteBillett.PaastigningsStasjon, SeteBillett.AvstigningsStasjon FROM SeteBillett
                    INNER JOIN Sete ON SeteBillett.SeteNr = Sete.SeteNr AND SeteBillett.VognID = Sete.VognID
                    INNER JOIN TogruteForekomst ON SeteBillett.TogruteforekomstID = TogruteForekomst.TogruteForekomstID
                    WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}''').fetchall()

    kjøpteSengeBilletter = cur.execute(f'''SELECT Seng.SengNr, Seng.VognID, TogruteForekomst.TogruteForekomstID, SengeBillett.PaastigningsStasjon, SengeBillett.AvstigningsStasjon FROM SengeBillett
                    INNER JOIN Seng ON SengeBillett.SengNr = Seng.SengNr AND SengeBillett.VognID = Seng.VognID
                    INNER JOIN TogruteForekomst ON SengeBillett.TogruteforekomstID = TogruteForekomst.TogruteForekomstID
                    WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}''').fetchall()


    kjøpteBilletter = kjøpteSeteBilletter + kjøpteSengeBilletter
    # Finner ledige seter
    muligSeteBilletter = cur.execute(f'''SELECT Sete.SeteNR, Sete.VognID, TogruteForekomst.TogruteForekomstID FROM Sete 
                INNER JOIN VognITogrute ON Sete.VognID = VognITogrute.VognID
                INNER JOIN Togrute ON Togrute.TogruteID = VognITogrute.TogruteID
                INNER JOIN TogruteForekomst ON Togrute.TogruteID = TogruteForekomst.TogruteID
                WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}''').fetchall()


    muligSengeBilletter =cur.execute(f'''SELECT Seng.SengNr, Seng.VognID, TogruteForekomst.TogruteForekomstID FROM Seng 
                INNER JOIN VognITogrute ON Seng.VognID = VognITogrute.VognID
                INNER JOIN Togrute ON Togrute.TogruteID = VognITogrute.TogruteID
                INNER JOIN TogruteForekomst ON Togrute.TogruteID = TogruteForekomst.TogruteID
                WHERE TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}''').fetchall()

    muligBilletter = []
    for b in muligSeteBilletter:
        muligBilletter.append((b[0], b[1], b[2], "Sete"))
    for b in muligSengeBilletter:
        muligBilletter.append((b[0], b[1], b[2], "Seng"))



    def kjøptAvBruker(billettID, email):
        ticks = cur.execute(f'''SELECT * FROM SengeBillett
                    INNER JOIN BillettKjoep ON SengeBillett.BestillingsID = BillettKjoep.BestillingsID
                    WHERE BillettKjoep.KjoeptAv = {email}
                    AND SengeBillett.BillettID = {billettID}''').fetchall()
        return len(ticks) != 0


    # Fjerner billetter fra outputen dersom den er booket på en delstrekning på ønsket strekning
    for billett in kjøpteBilletter:
        kjøptPaastigningNr = stasjonNr(billett[3], TogruteForekomstID)
        kjøptAvstigningNr = stasjonNr(billett[4], TogruteForekomstID)

        if(intersection(stasjonerMellom(startstasjonNr, endestasjonNr, TogruteForekomstID), stasjonerMellom(kjøptPaastigningNr, kjøptAvstigningNr, TogruteForekomstID))):
            for i in range(len(muligBilletter)):
                if(muligBilletter[i] != "Opptatt"):
                    if(muligBilletter[i][3] == "Sete"):
                        if((muligBilletter[i][0] == billett[0]) and (muligBilletter[i][1] == billett[1])):
                            muligBilletter[i] = "Opptatt"
                            continue
                    else:
                        if(((muligBilletter[i][0]-1)//2 == (billett[0]-1)//2) and ((muligBilletter[i][1]) == (billett[1]))):
                            muligBilletter[i] = "Opptatt"
                            continue


    for i in range(len(muligBilletter)):
        if(muligBilletter[i] == "Opptatt"):
            continue
        muligBilletter[i] = (muligBilletter[i][0], muligBilletter[i][1], muligBilletter[i][2],  muligBilletter[i][3], cur.execute(f'''SELECT RekkefoelgeNr FROM Togrute
                    INNER JOIN TogruteForekomst ON Togrute.TogruteID = TogruteForekomst.TogruteID
                    INNER JOIN VognITogrute ON VognITogrute.TogruteID = Togrute.TogruteID
                    WHERE VognITogrute.VognID = {muligBilletter[i][1]}
                    AND TogruteForekomst.TogruteForekomstID = {TogruteForekomstID}''').fetchall()[0][0])


    for i in range(len(muligBilletter)):
        if(muligBilletter[i] == "Opptatt"):
            print(f"Opptatt")
        else:
            if(muligBilletter[i][3] == "Sete"):
                print(f"Sete {muligBilletter[i][0]} Vogn {muligBilletter[i][4]} | {i}")
            else:
                print(f"Seng {muligBilletter[i][0]} Vogn {muligBilletter[i][4]} | {i}")


    seteValg = ""
    x = True
    while x:
        seteValg = input("Velg billetter ved å velge tallet til høyre, og separer billeter med mellomrom: f.eks. billett 1 og 3: blir 1 3\n Skal du bestille flere sengebilletter i én kupé må du velge begge nå\n")
        seteValg = seteValg.split(" ")
        for i in range(len(seteValg)):
            if muligBilletter[int(seteValg[i])] == "Opptatt":
                print(f"Billett {seteValg[i]} er opptatt")
                x = True
                break
            else:
                x = False
                break
            

    billetKjøpID = cur.execute(f'''SELECT MAX(BestillingsID) FROM BillettKjoep''').fetchall()[0][0]+1
    cur.execute(f'''INSERT INTO BillettKjoep (BestillingsID, kjoeptAv) VALUES ({billetKjøpID},"{BrukerEmail}")''')

    for kjøpSete in seteValg:
        billett = muligBilletter[int(kjøpSete)]
        if(billett[3] == "Sete"):
            cur.execute(f'''INSERT INTO SeteBillett (BestillingsID, SeteNr, VognID, TogruteForekomstID, PaastigningsStasjon, AvstigningsStasjon)
                        VALUES ({billetKjøpID}, {int(billett[0])}, {int(billett[1])}, {TogruteForekomstID}, "{startstasjon}", "{endestasjon}")''')
        else:
            cur.execute(f'''INSERT INTO SengeBillett (BestillingsID, SengNr, VognID, TogruteForekomstID, PaastigningsStasjon, AvstigningsStasjon)
                        VALUES ({billetKjøpID}, {int(billett[0])}, {int(billett[1])}, {TogruteForekomstID}, "{startstasjon}", "{endestasjon}")''')
        

    con.commit()