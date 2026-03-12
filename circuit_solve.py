#------------------------------------------------------------#
#----------------------circuit_solve.py----------------------#
#------------------------------------------------------------#
"""
Projekt: Analyse elektrischer Netzwerke
Autoren: Anton Gebauer, Anna-Maria Hartfelder, Jakub Waschow
Datum: 09.03.2026 
Beschreibung: Dieses Modul beschäftigt sich ausschließlich mit der Berechnung der Matrizen.
"""

import numpy as np

#------------------------------------------------------------#
#------------------Matrixaufbau und Lösung-------------------#
#------------------------------------------------------------#

def build_simple_mesh_matrix(R_self, R_shared):               #Baut eine Maschenmatrix basierend auf Eigenwiderständen und gemeinsamen Widerständen auf.
    """
    R_self: Liste der Eigenwiderstände
    R_shared: Matrix der gemeinsamen Widerstände
    """
    # Zählt die Anzahl der Maschen basierend auf der Liste der Eigenwiderstände
    Number_of_meshes = len(R_self)

    # Leere quadratische Masche erzeugen für die Widerstände
    A = np.zeros((Number_of_meshes, Number_of_meshes))

    # Füllt die Maschenmatrix basierend auf den Eigenwiderständen und den gemeinsamen Widerständen
    for i in range(Number_of_meshes):
        A[i, i] = R_self[i] + np.sum(R_shared[i]) # Eigenwiderstand plus Summe der gemeinsamen Widerstände in der i-ten Masche
        for j in range(Number_of_meshes):
           
            # Wenn i und j nicht gleich sind, wird der gemeinsame Widerstand von Masche i und j subtrahiert
            if i != j:
                A[i, j] = -R_shared[i][j]

    # Gibt die Maschenmatrix zurück
    return A

#------------------------------------------------------------#

def build_simple_nodal_matrix(R_between, R_ground):           #Baut eine Knotenmatrix basierend auf den Widerständen zwischen den Knoten und den Widerständen zur Masse auf.
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

#------------------------------------------------------------#

def solve_linear_system(A, b):                                #Löst das lineare Gleichungssystem Ax = b und gibt x zurück.

   try: 
        x = np.linalg.solve(A, b)  # np.linalg wird verwendet um das lineare Gleichungssystem zu lösen.
        return x
   except np.linalg.LinAlgError:  # Wenn die Matrix A singulär ist, wird eine Fehlermeldung ausgegeben und None zurückgegeben.
        print("Fehler: Das lineare Gleichungssystem ist singulär.")
        return None

