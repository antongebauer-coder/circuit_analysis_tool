# circuit_analysis_tool

Dieses Python‑Programm ermöglicht die Analyse elektrischer Gleichstromnetzwerke mittels Maschenstromanalyse (Mesh Analysis) und Knotenpotentialverfahren (Nodal Analysis).
Es unterstützt bis zu vier Maschen bzw. vier Knoten, erzeugt automatisch die zugehörigen Gleichungssysteme und löst diese numerisch mit numpy.
Das Tool eignet sich ideal für Studium, Laborübungen, Prüfungs­vorbereitung und schnelle technische Berechnungen.

Das Programm wurde entwickelt und getestet mit:
Python 3.11

----------------------------------------------------------------------------------------------

Beispiel: Maschenstromanalyse (2 Maschen)

Eingabe:  

Anzahl Maschen: 2  
Eigenwiderstand Masche 1: 10  
Eigenwiderstand Masche 2: 5  
Gemeinsamer Widerstand zwischen Masche 1 und 2: 2  
Maschenquelle Masche 1: 10  
Maschenquelle Masche 2: 0  

Ausgabe:  

Ergebnis Maschenströme (in A):  
  I_1 = 0.909091 A  
  I_2 = 0.259740 A  

----------------------------------------------------------------------------------------------

Beispiel: Knotenpotentialverfahren (2 Knoten)

Eingabe:  

Anzahl Knoten: 2  
Widerstand zwischen Knoten 1 und 2: 4  
Widerstand Knoten 1 zur Masse: 10  
Widerstand Knoten 2 zur Masse: 0  
Eingespeister Strom Knoten 1: 0.01  
Eingespeister Strom Knoten 2: 0  

Ausgabe:  

Ergebnis Knotenpotentiale (in V):
  V_1 = 0.0666667 V  
  V_2 = 0.0166667 V

----------------------------------------------------------------------------------------------

Teammitglieder
- Anton Gebauer - Dokumentation, Tests & Versionierung
- Anna-Maria Hartfelder - Sovler & Mathematischer Kern
- Jakub Warschow - Eingabesystem & Benutzerführung 
