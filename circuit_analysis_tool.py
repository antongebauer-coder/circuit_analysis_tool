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

#-------------------------------------------------------------
#--------Grundstruktur für das Eingabesystem------------------
#-------------------------------------------------------------

def input_int(prompt):
   
    #Liest später eine ganze Zahl ein.
   
    value = int(input(prompt))
    return value

#-------------------------------------------------------------

def input_float(prompt):
    
    #Liest später eine Fließkommazahl ein.
    
    value = float(input(prompt))
    return value

#-------------------------------------------------------------

def input_float_list(n, text):
    """
    Liest n Fließkommazahlen ein und gibt sie als Liste zurück.
    """
    values = []
    for i in range(n):
        v = input_float(f"{text} {i+1}: ")
        values.append(v)
    return values

#-------------------------------------------------------------

def input_matrix(n, text):
    """
    Liest eine einfache n×n-Matrix ein.
    Noch ohne Symmetrie oder Validierung.
    """
    M = []
    for i in range(n):
        row = []
        for j in range(n):
            v = input_float(f"{text} [{i+1},{j+1}]: ")
            row.append(v)
        M.append(row)
    return M

#-------------------------------------------------------------
#--------------Analysefunktionen------------------------------
#-------------------------------------------------------------

def mesh_analysis():                                          #Funktion Maschenstromanalyse
    print("\nMaschenstromanalyse (Mesh)")

    n = input_int("Anzahl Maschen: ")

    # Eigenwiderstände
    R_self = []
    for i in range(n):
        R_self.append(input_float(f"Eigenwiderstand Masche {i+1}: "))

    # Gemeinsame Widerstände
    R_shared = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            val = input_float(f"Gemeinsamer Widerstand zwischen Masche {i+1} und {j+1}: ")
            R_shared[i][j] = val
            R_shared[j][i] = val

    # Quellen
    V = []
    for i in range(n):
        V.append(input_float(f"Maschenquelle Masche {i+1}: "))

    # Matrix aufbauen
    A = build_simple_mesh_matrix(R_self, R_shared)

    # Lösen
    I = solve_linear_system(A, np.array(V))

    # Ausgabe
    print("\nErgebnis Maschenströme (in A):")
    for i, val in enumerate(I, start=1):
        print(f"  I_{i} = {val:.6f} A")

#-------------------------------------------------------------

def nodal_analysis():
    print("\nKnotenpotentialverfahren (Nodal)")

    n = input_int("Anzahl Knoten: ")

    # Widerstände zwischen Knoten
    R_between = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            val = input_float(f"Widerstand zwischen Knoten {i+1} und {j+1}: ")
            R_between[i][j] = val
            R_between[j][i] = val

    # Widerstände zur Masse
    R_ground = []
    for i in range(n):
        R_ground.append(input_float(f"Widerstand Knoten {i+1} zur Masse: "))

    # Eingespeiste Ströme
    I = []
    for i in range(n):
        I.append(input_float(f"Eingespeister Strom Knoten {i+1}: "))

    # Matrix aufbauen
    G = build_simple_nodal_matrix(R_between, R_ground)

    # Lösen
    V = solve_linear_system(G, np.array(I))

    # Ausgabe
    print("\nErgebnis Knotenpotentiale (in V):")
    for i, val in enumerate(V, start=1):
        print(f"  V_{i} = {val:.6f} V")

#-------------------------------------------------------------

def build_simple_mesh_matrix(R_self, R_shared):
    """
    Erstes Grundgerüst für eine Maschenmatrix.
    R_self: Liste der Eigenwiderstände
    R_shared: Matrix der gemeinsamen Widerstände
    """
    # Zählt die Anzahl der Maschen basierend auf der Liste der Eigenwiderstände
    Number_of_meshes = len(R_self)

    # Leere quadratische Masche erzeugen für die Widerstände
    A = np.zeros((Number_of_meshes, Number_of_meshes))

    # Füllt die Maschenmatrix basierend auf den Eigenwiderständen und den gemeinsamen Widerständen
    for i in range(Number_of_meshes):
        A[i, i] = R_self[i] + np.sum(R_shared[i])
        for j in range(Number_of_meshes):
           
            # Wenn i und j nicht gleich sind, wird der gemeinsame Widerstand von Masche i und j subtrahiert
            if i != j:
                A[i, j] = -R_shared[i][j]

    # Gibt die Maschenmatrix zurück
    return A

#-------------------------------------------------------------

def build_simple_nodal_matrix(R_between, R_ground):
    """
    Erstes Grundgerüst für eine Leitwertmatrix.
    R_between: Matrix der Widerstände zwischen Knoten
    R_ground: Liste der Widerstände zur Masse
    """
    # Zählt die Anzahl der Knoten basierend auf der Liste der Widerstände zur Masse
    Number_of_nodes = len(R_ground)

    # Leere quadratische Matrix für die Leitwerte erzeugen
    G = np.zeros((Number_of_nodes, Number_of_nodes))

    # Füllt die Leitwertmatrix basierend auf den Widerständen zwischen den Knoten und den Widerständen zur Masse
    for i in range(Number_of_nodes):
        sum_g = 0 
        for j in range(Number_of_nodes):  
        
            if i != j and R_between[i][j] > 0:
                gij = 1 / R_between[i][j]
                G[i, j] = -gij
                sum_g += gij

        if R_ground[i] > 0:   # Wenn es einen Widerstand zur Masse gibt, wird der Leitwert addiert
            sum_g += 1 / R_ground[i]

        G[i, i] = sum_g 

    # Gibt die Leitwertmatrix zurück
    return G

#-------------------------------------------------------------

def solve_linear_system(A, b):

   #Löst das lineare Gleichungssystem A * x = b.
   x = np.linalg.solve(A, b)
   return x


###########################################################################################################

def main():
    print("Wähle Methode:")
    print("  1 - Maschenstromanalyse (Mesh)")
    print("  2 - Knotenpotentialverfahren (Nodal)")
    choice = int(input("Auswahl (1 oder 2): "))
    if choice == 1:
        mesh_analysis()
    else:
        nodal_analysis()

#############################################################################################################

if __name__ == "__main__":
    main()