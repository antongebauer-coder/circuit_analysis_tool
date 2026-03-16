Testcase 1 – Korrekte Berechnung (Maschenstromanalyse)

Auswahl (1 oder 2): 1
Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Maschen: 2

Eigenwiderstand Masche 1: 10
Eigenwiderstand Masche 2: 15

Gemeinsamer Widerstand zwischen Masche 1 und 2: 5

Maschenquelle Masche 1: 12
Maschenquelle Masche 2: 0

Ergebnis Maschenströme (in A):

I_1 = 0.872727 A
I_2 = 0.218182 A

----------------------------------------------------------------------------------------------

Testcase 2 – Fehlerhafte Eingabe (Buchstaben)

Auswahl (1 oder 2): a

Ungültige Eingabe. Bitte eine gültige Zahl eingeben.

Auswahl (1 oder 2): 2
Benötigst du Hilfe bei dem Verfahren? (j/n): n

...

----------------------------------------------------------------------------------------------

Testcase 3 – Negative Werte (physikalisch ungültig)

Auswahl (1 oder 2): 2
Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Knoten: 2

Widerstand zwischen Knoten 1 und 2: -5

Der Widerstand zwischen Knoten darf nicht negativ sein. Bitte erneut eingeben.

Widerstand zwischen Knoten 1 und 2: 5

...

----------------------------------------------------------------------------------------------

Testcase 4 – Grenzwertprüfung (zu große Anzahl)

Auswahl (1 oder 2): 1
Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Maschen: 15

Die Anzahl sollte 10 nicht überschreiten, um die Übersicht zu behalten.

Anzahl Maschen: 3

...

----------------------------------------------------------------------------------------------

Testcase 5 – Grenzwertprüfung (0 oder negative Anzahl)

Auswahl (1 oder 2): 2
Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Knoten: 0

Bitte eine positive ganze Zahl eingeben.

Anzahl Knoten: -3

Bitte eine positive ganze Zahl eingeben.

Anzahl Knoten: 2

...

----------------------------------------------------------------------------------------------

Testcase 6 – Singuläres Gleichungssystem

Auswahl (1 oder 2): 2
Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Knoten: 2

Widerstand zwischen Knoten 1 und 2: 10

Widerstand Knoten 1 zur Masse: 0
Widerstand Knoten 2 zur Masse: 0

Eingespeister Strom Knoten 1: 1
Eingespeister Strom Knoten 2: -1

Fehler: Das lineare Gleichungssystem ist singulär.
Die Knotenpotentiale konnten nicht berechnet werden.