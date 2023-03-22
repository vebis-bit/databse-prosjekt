CREATE TABLE Togrute (
    TogruteID INTEGER PRIMARY KEY,
    Dager TEXT NOT NULL,
    Hovedretning BOOLEAN NOT NULL,
    OperatoerID INTEGER NOT NULL,
    FOREIGN KEY (OperatoerID) REFERENCES Operatoer (OperatoerID)
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

CREATE TABLE Vogn (
    VognID INTEGER,
    OperatoerNavn TEXT NOT NULL,
    AntallRader INTEGER,
    SeterPerRad INTEGER,
    AntallKupeer INTEGER,
    FOREIGN KEY (OperatoerNavn) REFERENCES Operatoer (Navn)
        ON UPDATE CASCADE
);

CREATE TABLE VognITogrute(
	VognID INTEGER,
	TogruteID INTEGER,
	RekkefoelgeNr INTEGER,
	PRIMARY KEY(VognID, TogruteID),
	FOREIGN KEY (VognID) REFERENCES Vogn(VognID),
	FOREIGN KEY(TogruteId) REFERENCES Togrute(TogruteID)
);

CREATE TABLE Kunde (
 	KundeNr INTEGER PRIMARY KEY,
    RegistretAv INTEGER NOT NULL,
    Fornavn TEXT NOT NULL,
    Etternavn TEXT NOT NULL,
    Email TEXT NOT NULL,
    TelefonNummer TEXT NOT NULL,
    FOREIGN KEY (RegistretAv) REFERENCES Operatoer (OperatoerID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
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
    BestillingsID INTEGER PRIMARY KEY,
 	KjoeptAv INTEGER NOT NULL,
 	FOREIGN KEY (KjoeptAv) REFERENCES Kunde (KundeNr)
	    ON DELETE CASCADE
	    ON UPDATE CASCADE
);

CREATE TABLE SengeBillett (
    BillettID INTEGER PRIMARY KEY,
	BestillingsID INTEGER NOT NULL,
	KupeNr INTEGER NOT NULL,
	VognID INTEGER NOT NULL,
 	TogruteforekomstID INTEGER,
 	PaastigningsStasjon TEXT,
 	AvstigningsStasjon TEXT,
 	FOREIGN KEY (BestillingsID) REFERENCES BillettKjoep (BestillingsID),
 	FOREIGN KEY (KupeNr, VognID) REFERENCES Kupe (KupeNr, VognID),
    FOREIGN KEY (TogruteforekomstID) REFERENCES TogruteForekomst (TogruteforekomstID),
    FOREIGN KEY (PaastigningsStasjon) REFERENCES Stasjon(Navn),
    FOREIGN KEY (AvstigningsStasjon) REFERENCES Stasjon(Navn)
);

CREATE TABLE SeteBillett (
 	BillettID INTEGER PRIMARY KEY,
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
	Avgang TIME,
	Ankomst TIME,
	PRIMARY KEY (TogruteID, StasjonNavn),
	FOREIGN KEY (TogruteID) REFERENCES Togrute(TogruteID),
	FOREIGN KEY (StasjonNavn) REFERENCES Stasjon(Navn)
);

CREATE TABLE BanestrekningHarStasjon(
	BanestrekningNavn INTEGER NOT NULL,
	StasjonNavn TEXT NOT NULL,
	Posisjon INTEGER NOT NULL,
	PRIMARY KEY (BanestrekningNavn, StasjonNavn),
	FOREIGN KEY (BanestrekningNavn) REFERENCES BaneStrekning(Navn),
    FOREIGN KEY (StasjonNavn) REFERENCES Stasjon(Navn)


);

