INSERT INTO Operatoer VALUES ("SJ");

INSERT INTO VognType VALUES ("Sittevogn-1", "SJ", 3, 4, 0);
INSERT INTO VognType VALUES ("Sovevogn-1", "SJ", 0, 0, 4);


INSERT INTO Togrute(TogruteID, Dager, Hovedretning, OperatoerNavn) VALUES (1, "1111100", true, "SJ");

INSERT INTO TogruteBesoekerStasjon VALUES (1, "Trondheim", "07:47:00", "07:45:00");
INSERT INTO TogruteBesoekerStasjon VALUES (1, "Steinkjer", "09:51:00", "09:48:00");
INSERT INTO TogruteBesoekerStasjon VALUES (1, "Mosjøen", "13:20:00", "13:17:00");
INSERT INTO TogruteBesoekerStasjon VALUES (1, "Mo i Rana", "14:31:00", "14:28:00");
INSERT INTO TogruteBesoekerStasjon VALUES (1, "Fauske", "16:49:00", "16:46:00");
INSERT INTO TogruteBesoekerStasjon VALUES (1, "Bodø", "17:35:00", "17:33:00");

INSERT INTO Vogn (VognID, Vogntype, OperatoerNavn) VALUES (2, "Sittevogn-1", "SJ");

INSERT INTO VognITogrute VALUES (1, 1, 1);
INSERT INTO VognITogrute VALUES (1, 2, 2);

INSERT INTO Togrute(TogruteID, Dager, Hovedretning, OperatoerNavn) VALUES (13, "1111111", true, "SJ");

INSERT INTO TogruteBesoekerStasjon VALUES (13, "Trondheim", "23:02:00", "23:05:00");
INSERT INTO TogruteBesoekerStasjon VALUES (13, "Steinkjer", "00:54:00", "00:57:00");
INSERT INTO TogruteBesoekerStasjon VALUES (13, "Mosjøen", "04:38:00", "04:41:00");
INSERT INTO TogruteBesoekerStasjon VALUES (13, "Mo i Rana", "05:52:00", "05:55:00");
INSERT INTO TogruteBesoekerStasjon VALUES (13, "Fauske", "08:16:00", "08:19:00");
INSERT INTO TogruteBesoekerStasjon VALUES (13, "Bodø", "09:02:00", "09:05:00");

INSERT INTO Vogn (VognID, Vogntype, OperatoerNavn) VALUES (3, "Sittevogn-1", "SJ");
INSERT INTO Vogn (VognID, Vogntype, OperatoerNavn) VALUES (4, "Sovevogn-1", "SJ");

INSERT INTO VognITogrute VALUES (13, 3, 1);
INSERT INTO VognITogrute VALUES (13, 4, 2);

INSERT INTO Togrute(TogruteID, Dager, Hovedretning, OperatoerNavn) VALUES(52, "1111100", false, "SJ");

INSERT INTO TogruteBesoekerStasjon VALUES (52, "Mo i Rana", "08:08:00", "08:11:00");
INSERT INTO TogruteBesoekerStasjon VALUES (52, "Mosjøen", "09:11:00", "09:14:00");
INSERT INTO TogruteBesoekerStasjon VALUES (52, "Steinkjer", "12:28:00", "12:31:00");
INSERT INTO TogruteBesoekerStasjon VALUES (52, "Trondheim", "14:10:00", "14:13:00");

INSERT INTO Vogn (VognID, Vogntype, OperatoerNavn) VALUES (5, "Sittevogn-1", "SJ");

INSERT INTO VognITogrute VALUES (52, 5, 1);