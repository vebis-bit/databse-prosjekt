INSERT INTO Banestrekning VALUES ("NordlandsBanen");
INSERT INTO Stasjon VALUES ("Bodø", 4.1);
INSERT INTO Stasjon VALUES ("Fauske", 34.0);
INSERT INTO Stasjon VALUES ("Mo i Rana", 3.5);
INSERT INTO Stasjon VALUES ("Mosjøen", 6.8);
INSERT INTO Stasjon VALUES ("Steinkjer", 3.6);
INSERT INTO Stasjon VALUES ("Trondheim", 5.1);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Trondheim", 1);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Steinkjer", 2);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Mosjøen", 3);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Mo i Rana", 4);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Fauske", 5);
INSERT INTO BanestrekningHarStasjon VALUES ("NordlandsBanen", "Bodø", 6);
INSERT INTO DelStrekning VALUES ("Bodø", "Fauske", 60, false);
INSERT INTO DelStrekning VALUES ("Fauske", "Mo i Rana", 170, false);
INSERT INTO DelStrekning VALUES ("Mo i Rana", "Mosjøen", 90, false);
INSERT INTO DelStrekning VALUES ("Mosjøen", "Steinkjer", 280, false);
