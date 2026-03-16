#------------------------------------------------------------#
#---------------------------Header---------------------------#
#------------------------------------------------------------#

'''
Projekt: Analyse elektrischer Netzwerke
Autoren: Anton Gebauer, Anna-Maria Hartfelder, Jakub Waschow
Datum: 09.03.2026
Version: 3.3

Beschreibung:
Dieses Konsolenprogramm dient zur Analyse einfacher linearer
Gleichstromnetzwerke. Es unterstützt das Knotenpotentialverfahren
sowie die Maschenstromanalyse für kleine Schaltungen mit
Widerständen und Spannungsquellen.
'''

#------------------------------------------------------------#
#------------Grundstruktur für das Eingabesystem-------------#
#------------------------------------------------------------#

import numpy as np                                            # wird verwendet um mit Matrizen und linearen Gleichungssystemen zu arbeiten.
import tkinter as tk                                          # wird verwendet um die Hilfefenster für die Anleitungen zu erstellen.
import circuit_solve as cs                                    # wird verwendet um die Funktionen zum Aufbau der Matrizen und zum Lösen der linearen Gleichungssysteme zu nutzen.

def input_int(prompt):
        while True:
            try:
                value = int(input(prompt))
            
                if value <= 0:
                    print("Bitte eine positive ganze Zahl eingeben.")
                elif value > 10:
                    print("Die Anzahl sollte 10 nicht überschreiten, um die Übersicht zu behalten.")
                else:                
                    return value
                
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
#------------------------------------------------------------#

def input_float(prompt):                                      #Liest eine Fließkommazahl ein und gibt sie zurück.
    
    while True:
        try:
            value = float(input(prompt).replace(',', '.'))
            return value
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")

#------------------------------------------------------------#

def input_float_list(n, text):                                #Liest n Fließkommazahlen ein und gibt sie als Liste zurück.
    
    values = []
    for i in range(n):
        v = input_float(f"{text} {i+1}: ")
        values.append(v)
    return values

#------------------------------------------------------------#

def input_matrix(n, text):                                    #Liest eine einfache n×n-Matrix ein.
    
    M = []
    for i in range(n):
        row = []
        for j in range(n):
            v = input_float(f"{text} [{i+1},{j+1}]: ")
            row.append(v)
        M.append(row)
    return M

#------------------------------------------------------------#
#---------------------Analysefunktionen----------------------#
#------------------------------------------------------------#

def mesh_analysis():                                          #Maschenstromanalyse (Mesh)
    print("\nMaschenstromanalyse (Mesh)")

    n = input_int("Anzahl Maschen: ")

    # Eigenwiderstände
    R_self = []
    for i in range(n):
        while True:
            r = input_float(f"Eigenwiderstand Masche {i+1} (in Ohm): ")
            if r < 0:
                print("Der Eigenwiderstand muss positiv sein. Bitte erneut eingeben.")
            else:
                R_self.append(r)
                break
        

    # Gemeinsame Widerstände
    R_shared = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            while True:
                val = input_float(f"Gemeinsamer Widerstand zwischen Masche {i+1} und {j+1} (in Ohm): ")
                if val < 0:
                    print("Der gemeinsame Widerstand muss positiv sein. Bitte erneut eingeben.")
                else:
                    break
            R_shared[i][j] = val
            R_shared[j][i] = val

    # Quellen
    V = []
    for i in range(n):
        V.append(input_float(f"Maschenquelle Masche {i+1} (in V): "))

    # Matrix aufbauen
    A = cs.build_simple_mesh_matrix(R_self, R_shared)

    # Lösen
    I = cs.solve_linear_system(A, np.array(V))                #wird verwendet um die Maschenströme zu berechnen, indem das lineare Gleichungssystem Ax = V gelöst wird, wobei A die Maschenmatrix und V die Maschenquellen sind.

    if I is None:
        print("Die Maschenströme konnten nicht berechnet werden.")
        return

    # Ausgabe
    print("\nErgebnis Maschenströme (in A):")
    for i, val in enumerate(I, start=1): #
        print(f"  I_{i} = {val:.6f} A")

#------------------------------------------------------------#

def nodal_analysis():                                         #knotenpotentialverfahren (Nodal)
    print("\nKnotenpotentialverfahren (Nodal)")

    n = input_int("Anzahl Knoten: ")

    # Widerstände zwischen Knoten
    R_between = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            while True:
                val = input_float(f"Widerstand zwischen Knoten {i+1} und {j+1} (in Ohm): ")
                if val < 0:
                    print("Der Widerstand zwischen Knoten darf nicht negativ sein. Bitte erneut eingeben.")
                else:      
                    R_between[i][j] = val
                    R_between[j][i] = val              
                    break

                

    # Widerstände zur Masse
    R_ground = []
    for i in range(n):
        while True:
            r = input_float(f"Widerstand Knoten {i+1} zur Masse (in Ohm): ")
            if r < 0:
                print("Der Widerstand zur Masse darf nicht negativ sein. Bitte erneut eingeben.")
            else:    
                R_ground.append(r)
                break

    # Eingespeiste Ströme
    I = []
    for i in range(n):
        I.append(input_float(f"Eingespeister Strom Knoten {i+1} (in A): "))

    # Matrix aufbauen
    G = cs.build_simple_nodal_matrix(R_between, R_ground)

    # Lösen
    V = cs.solve_linear_system(G, np.array(I))                #wird verwendet um die Knotenpotentiale zu berechnen, indem das lineare Gleichungssystem Gx = I gelöst wird, wobei G die Leitwertmatrix und I die eingespeisten Ströme sind.

    if V is None:
        print("Die Knotenpotentiale konnten nicht berechnet werden.")
        return

    # Ausgabe
    print("\nErgebnis Knotenpotentiale (in V):")
    for i, val in enumerate(V, start=1):
        print(f"  V_{i} = {val:.6f} V")


##############################################################
#-----------------------Hilfefunktionen----------------------#
##############################################################
def show_mesh_help():
   
   #Fenster erstellen
   root = tk.Tk()                                             #wird verwendet um ein neues Fenster zu erstellen
   root.title("Anleitung: Maschenstromverfahren") 
   root.geometry("720x520")

   # Fenster in den Vordergrund bringen
   root.lift() 
   root.attributes("-topmost", True)
   root.after(200, lambda: root.attributes("-topmost", False))
   root.focus_force()

   text = """
    MASCHENSTROMANALYSE (MESH) - KURZANLEITUNG

    1. Voraussetzungen
    Im Netzwerk dürfen sich nur Widerstände und Spannungsquellen befinden.
    Stromquellen oder abhängige Quellen müssen vorher umgewandelt werden.

    2. Maschen festlegen
    Bestimme die Anzahl der Maschen im Netzwerk und legen sie
    für jede Masche eine Stromrichtung fest.

    3. Eigenwiderstände
    Gehe jede Masche entlang und gebe alle Widerstände an,
    die ausschließlich in dieser Masche liegen.

    4. Kopplungswiderstände
    Überprüfe für jedes Maschenpaar, ob ein gemeinsamer Widerstand
    existiert. Diese Widerstände nennt man Kopplungswiderstände.

    5. Vorzeichen der Kopplungswiderstände
    Wenn die Maschenströme durch den gemeinsamen Widerstand in
    die gleiche Richtung fließen, ist der Widerstand positiv.
    Fließen sie entgegengesetzt, ist der Widerstand negativ.

    6. Maschenquellen
    Alle Spannungsquellen innerhalb einer Masche werden berücksichtigt:
    - Verlaufen sie entgegen der Maschenstromrichtung → positiv
    - Verlaufen sie in Richtung des Maschenstroms → negativ
    """
    

   label = tk.Label(root, text=text, justify=tk.LEFT, padx=10, pady=10)
   label.pack()

#------------------------------------------------------------#

def show_nodal_help():

    # Fenster erstellen
    root = tk.Tk()
    root.title("Anleitung: Knotenpotentialverfahren")
    root.geometry("720x520")
    
    # Fenster in den Vordergrund bringen
    root.lift() 
    root.attributes("-topmost", True)
    root.after(200, lambda: root.attributes("-topmost", False))
    root.focus_force()

    text = """
    KNOTENPOTENZIALANALYSE (NODAL) - KURZANLEITUNG

    1. Voraussetzungen
    Im Netzwerk dürfen sich nur Widerstände und Stromquellen befinden.
    Spannungsquellen müssen vorher umgewandelt werden.

    2. Bezugsknoten festlegen
    Ein Knoten wird als Bezugsknoten gewählt und auf 0 V gesetzt.
    Alle anderen Knotenpotentiale werden relativ zu diesem berechnet.

    3. Widerstände zur Masse
    Für jeden Knoten werden die Widerstände eingegeben,
    die direkt vom Knoten weg führen.

    4. Widerstände zwischen den Knoten
    Für jedes Knotenpaar wird angegeben, ob ein Widerstand
    zwischen diesen Knoten existiert.
    Falls kein Widerstand vorhanden ist, wird 0 eingegeben.

    5. Stromquellenströme
    Alle Ströme, die in den Knoten fließen, werden positiv eingegeben.
    Alle Ströme, die aus dem Knoten herausfließen, werden negativ eingegeben.
    """
    
    label = tk.Label(root, text=text, justify=tk.LEFT, padx=10, pady=10)
    label.pack()

##############################################################
#-----------------------Hauptprogramm------------------------#
##############################################################

def main():                                                   #Hauptfunktion, Auswahlaufforderung der Analysemethode, ruft entsprehende Funktion auf.

    while True:
        print("Wähle Methode:")
        print("  1 - Maschenstromanalyse (Mesh)")
        print("  2 - Knotenpotentialverfahren (Nodal)")
        
        while True:
            try:
                choice = int(input("Auswahl (1 oder 2): "))
                
                if choice == 1:
                    need_help = input("Benötigst du Hilfe bei dem Verfahren? (j/n): ").strip().lower()
                    #Wenn der Benutzer Hilfe benötigt, wird die Hilfefunktion für das Maschenstromverfahren aufgerufen.
                    while True:
                        if need_help == 'j':
                            show_mesh_help()
                            break
                        elif need_help == 'n':
                            break
                        else:
                            print("Ungültige Eingabe. Bitte 'j' für Ja oder 'n' für Nein eingeben.")
                            need_help = input("Benötigst du Hilfe bei dem Verfahren? (j/n): ").strip().lower()
                            pass

                    mesh_analysis()
                    break
                elif choice == 2:
                    need_help = input("Benötigst du Hilfe bei dem Verfahren? (j/n): ").strip().lower()
                    #Wenn der Benutzer Hilfe benötigt, wird die Hilfefunktion für das Knotenpotentialverfahren aufgerufen.
                    while True:
                        if need_help == 'j':
                            show_nodal_help()
                            break
                        elif need_help == 'n':
                            break
                        else:
                            print("Ungültige Eingabe. Bitte 'j' für Ja oder 'n' für Nein eingeben.")
                            need_help = input("Benötigst du Hilfe bei dem Verfahren? (j/n): ").strip().lower()
                        continue

                    nodal_analysis()
                    break
                else:
                    print("Ungültige Auswahl. Bitte 1 oder 2 eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")

        while True:
            cont = input("Möchtest du eine weitere Analyse durchführen? (j/n): ").strip().lower()
            if cont == 'j':
                break
            elif cont == 'n':
                print("Programm wird beendet.")
                return
            else:
                print("Ungültige Eingabe. Bitte 'j' für Ja oder 'n' für Nein eingeben.")    

##############################################################
#------------------------------------------------------------#
##############################################################

if __name__ == "__main__":
    main()