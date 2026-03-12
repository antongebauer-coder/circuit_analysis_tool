# circuit_analysis_tool

Dieses Python‑Programm ermöglicht die Analyse elektrischer Gleichstromnetzwerke mittels Maschenstromanalyse (Mesh Analysis) und Knotenpotentialverfahren (Nodal Analysis).
Es unterstützt bis zu vier Maschen bzw. vier Knoten, erzeugt automatisch die zugehörigen Gleichungssysteme und löst diese numerisch mit numpy.
Das Tool eignet sich ideal für Studium, Laborübungen, Prüfungs­vorbereitung und schnelle technische Berechnungen.

Das Programm wurde entwickelt und getestet mit:
Python 3.11

Teammitglieder
- Anton Gebauer - Dokumentation, Tests & Versionierung
- Anna-Maria Hartfelder - Sovler & Mathematischer Kern
- Jakub Warschow - Eingabesystem & Benutzerführung 

----------------------------------------------------------------------------------------------------
Beispielhafte Nutzung 
- Eingaben:
Wähle Methode:
  1 - Maschenstromanalyse (Mesh)
  2 - Knotenpotentialverfahren (Nodal)
Auswahl (1 oder 2): 1

Benötigst du Hilfe bei dem Verfahren? (j/n): n

Anzahl Maschen: 2
Eigenwiderstand Masche 1 (in Ohm): 15
Eigenwiderstand Masche 2 (in Ohm): 10
Gemeinsamer Widerstand zwischen Masche 1 und 2 (in Ohm): 5
Maschenquelle Masche 1 (in V): 20
Maschenquelle Masche 2 (in V): 25

- Ausgaben:
Ergebnis Maschenströme (in A):
  I_1 = 1.545455 A
  I_2 = 2.181818 A

Danach kommt eine weiter Frage:
Möchtest du eine weitere Analyse durchführen? (j/n): n

Ausgabe: Programm wird beendet.


