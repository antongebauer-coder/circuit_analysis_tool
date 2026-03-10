'''
Projekt: Analyse elektrischer Netzwerke
Autoren: Anton Gebauer, Anna-Maria Hartfelder, Jakub Waschow
Datum: 09.03.2026
Version: 0.1

Beschreibung:
Dieses Konsolenprogramm dient zur Analyse einfacher linearer
Gleichstromnetzwerke. Es unterstützt das Knotenpotentialverfahren
sowie die Maschenstromanalyse für kleine Schaltungen mit
Widerständen und Spannungsquellen.
'''

import numpy as np

def mesh_analysis():
    pass

def nodal_analysis():
    pass

def main():
    print("Wähle Methode:")
    print("  1 - Maschenstromanalyse (Mesh)")
    print("  2 - Knotenpotentialverfahren (Nodal)")
    choice = int(input("Auswahl (1 oder 2): "))
    if choice == 1:
        mesh_analysis()
    else:
        nodal_analysis()

if __name__ == "__main__":
    main()