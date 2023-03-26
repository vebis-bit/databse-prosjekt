CREATE TABLE Togrute (
    TogruteID INTEGER PRIMARY KEY,
    Dager TEXT NOT NULL,
    Hovedretning BOOLEAN NOT NULL,
    OperatoerNavn TEXT NOT NULL,
    FOREIGN KEY (OperatoerNavn) REFERENCES Operatoer (Navn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE TogruteForekomst (
	TogruteForekomstID INTEGER NOT NULL,
	Dag INTEGER NOT NULL,
	Maaned INTEGER NOT NULL,
	Aar INTEGER NOT NULL,
	TogruteID INTEGER NOT NULL,
	PRIMARY KEY(TogruteForekomstID),
	FOREIGN KEY (TogruteID) REFERENCES Togrute (TogruteID)
        ON DELETE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE BesoekerStasjon (
    TogruteID INTEGER NOT NULL,
    StasjonNavn TEXT NOT NULL,
    Avgang TIME,
    Ankomst TIME,
    RekkefoelgeNr INTEGER,
    PRIMARY KEY (TogruteID, StasjonNavn),
    FOREIGN KEY (TogruteID) REFERENCES Togrute (TogruteID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (StasjonNavn) REFERENCES Stasjon (Navn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Stasjon (
    Navn TEXT PRIMARY KEY,
    Moh INTEGER NOT NULL
);

CREATE TABLE DelStrekning (
    StartStasjon TEXT NOT NULL,
    EndeStasjon TEXT NOT NULL,
    Distanse REAL NOT NULL,
    DobbeltSpor BOOLEAN NOT NULL,
    PRIMARY KEY (StartStasjon, EndeStasjon),
    FOREIGN KEY (StartStasjon) REFERENCES Stasjon (Navn)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (EndeStasjon) REFERENCES Stasjon (Navn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Banestrekning (
  	Navn TEXT PRIMARY KEY
);

CREATE TABLE Operatoer (
 	Navn TEXT PRIMARY KEY
);

CREATE TABLE VognType(
    Navn TEXT NOT NULL,
    OperatoerNavn TEXT NOT NULL
    AntallRader INTEGER,
    SeterPerRad INTEGER,
    AntallKupeer INTEGER,
    PRIMARY KEY (Navn, OperatoerNavn),
    FOREIGN KEY (OperatoerNavn) REFERENCES Operatoer (Navn)
)

CREATE TABLE Vogn (
    VognID INTEGER PRIMARY KEY,
    Vogntype TEXT,
    OperatoerNavn TEXT,
    FOREIGN KEY (Vogntype, OperatoerNavn) REFERENCES VognType(Navn, OperatoerNavn)
);

CREATE TABLE VognITogrute(
    TogruteID INTEGER,
	VognID INTEGER,
	RekkefoelgeNr INTEGER,
	PRIMARY KEY(TogruteID, VognID),
	FOREIGN KEY (VognID) REFERENCES Vogn(VognID),
	FOREIGN KEY(TogruteId) REFERENCES Togrute(TogruteID)
);

CREATE TABLE Kunde (
    Fornavn TEXT NOT NULL,
    Etternavn TEXT NOT NULL,
    Email TEXT NOT NULL PRIMARY KEY,
    TelefonNummer TEXT NOT NULL,
);

CREATE TABLE Kupe (
    KupeNr INTEGER NOT NULL,
    VognID INTEGER NOT NULL,
    PRIMARY KEY (KupeNr, VognID),
    FOREIGN KEY (VognID) REFERENCES Vogn (VognID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Sete (
 	SeteNr INTEGER NOT NULL,
 	VognID INTEGER NOT NULL,
 	PRIMARY KEY (SeteNr, VognID)
	FOREIGN KEY (VognID) REFERENCES Vogn (VognID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE BillettKjoep (
    BestillingsID INTEGER PRIMARY KEY AUTOINCREMENT,
 	KjoeptAv TEXT NOT NULL,
 	FOREIGN KEY (KjoeptAv) REFERENCES Kunde (Email)
	    ON DELETE CASCADE
	    ON UPDATE CASCADE
);

CREATE TABLE SengeBillett (
    BillettID INTEGER PRIMARY KEY AUTOINCREMENT,
	BestillingsID INTEGER NOT NULL,
	SengNR INTEGER NOT NULL,
	VognID INTEGER NOT NULL,
 	TogruteforekomstID INTEGER,
 	PaastigningsStasjon TEXT,
 	AvstigningsStasjon TEXT,
 	FOREIGN KEY (BestillingsID) REFERENCES BillettKjoep (BestillingsID),
 	FOREIGN KEY (SengNR, VognID) REFERENCES Seng (SengNR, VognID),
    FOREIGN KEY (TogruteforekomstID) REFERENCES TogruteForekomst (TogruteforekomstID),
    FOREIGN KEY (PaastigningsStasjon) REFERENCES Stasjon(Navn),
    FOREIGN KEY (AvstigningsStasjon) REFERENCES Stasjon(Navn)
);

CREATE TABLE SeteBillett (
 	BillettID INTEGER PRIMARY KEY AUTOINCREMENT,
    BestillingsID INTEGER NOT NULL,
 	SeteNr INTEGER NOT NULL,
	VognID INTEGER NOT NULL,
 	TogruteforekomstID INTEGER,
 	PaastigningsStasjon TEXT,
 	AvstigningsStasjon TEXT,
    FOREIGN KEY (BestillingsID) REFERENCES BillettKjoep (BestillingsID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
 	FOREIGN KEY (SeteNr, VognID) REFERENCES Sete (SeteNr, VognID),
    FOREIGN KEY (TogruteforekomstID) REFERENCES TogruteForekomst (TogruteforekomstID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (PaastigningsStasjon) REFERENCES Stasjon(Navn),
 	FOREIGN KEY (AvstigningsStasjon) REFERENCES Stasjon(Navn)
);

CREATE TABLE TogruteBesoekerStasjon(
	TogruteID INTEGER NOT NULL,
	StasjonNavn TEXT NOT NULL,
	Avgang TIME NOT NULL,
	Ankomst TIME NOT NULL,
    RekkefoelgeNr INT NOT NULL
	PRIMARY KEY (TogruteID, StasjonNavn),
	FOREIGN KEY (TogruteID) REFERENCES Togrute(TogruteID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY (StasjonNavn) REFERENCES Stasjon(Navn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE BanestrekningHarStasjon(
	BanestrekningNavn INTEGER NOT NULL,
	StasjonNavn TEXT NOT NULL,
	Posisjon INTEGER NOT NULL,
	PRIMARY KEY (BanestrekningNavn, StasjonNavn),
	FOREIGN KEY (BanestrekningNavn) REFERENCES BaneStrekning(Navn),
    FOREIGN KEY (StasjonNavn) REFERENCES Stasjon(Navn)


);

