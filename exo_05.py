"""
Exercice 5 : plus court chemin dans un labyrinthe (moyen, 30 min)

Écris plus_court_chemin(grille: list[str]) -> int.

S est le départ, E l’arrivée, # un mur, . une case libre.
On se déplace en haut, en bas, à gauche ou à droite.
Renvoie le nombre minimal de déplacements, ou -1 si l’arrivée est inaccessible.

grille = [
    "S.#.",
    ".##.",
    "...E",
]
plus_court_chemin(grille)  # 5

Question à te poser : pourquoi un parcours en largeur (BFS) donne le plus court
chemin alors qu’un parcours en profondeur (DFS) non ?
"""