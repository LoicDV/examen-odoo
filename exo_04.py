"""
Exercice 4 : fusion d’intervalles (moyen, 25 min)

Écris fusionner(intervalles: list[list[int]]) -> list[list[int]], qui fusionne
les intervalles qui se chevauchent ou se touchent. L’entrée n’est pas triée.

fusionner([[8, 10], [1, 3], [2, 6], [15, 18]])  # [[1, 6], [8, 10], [15, 18]]
fusionner([[1, 4], [4, 5]])                     # [[1, 5]]
fusionner([])                                   # []

Contexte métier : fusionner des créneaux de réservation d’une salle.
"""

"""
def fusionner(intervalles:list[list[int]]) -> list[list[int]]:
    if not intervalles:
        return []

    intervalles = sorted(intervalles, key=lambda item : -item[0])

    ans = []
    inter = intervalles.pop()
    for elem in intervalles[-1:-len(intervalles)-1:-1]:
        if inter[0] == elem[0] or elem[0] <= inter[1]:
            inter[1] = max(elem[1], inter[1])
        else:
            ans.append(inter)
            inter = elem

    ans.append(inter)
    return ans

if __name__ == "__main__":
    assert fusionner([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert fusionner([[1, 4], [4, 5]]) == [[1, 5]]
    assert fusionner([]) == []
    print("Tous les tests sont passés")
"""

"""
CORRECTION
"""

def fusionner(intervalles: list[list[int]]) -> list[list[int]]:
    """Fusionne les intervalles qui se chevauchent ou se touchent.

    Ne modifie pas la liste reçue.
    """
    if not intervalles:
        return []

    tries = sorted(intervalles)
    resultat = [list(tries[0])]          # copie : on ne touche pas à l'entrée
    for debut, fin in tries[1:]:
        dernier = resultat[-1]
        if debut <= dernier[1]:
            dernier[1] = max(dernier[1], fin)
        else:
            resultat.append([debut, fin])
    return resultat


if __name__ == "__main__":
    assert fusionner([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert fusionner([[1, 4], [4, 5]]) == [[1, 5]]
    assert fusionner([]) == []
    # un seul intervalle, intervalle inclus, même début
    assert fusionner([[3, 7]]) == [[3, 7]]
    assert fusionner([[1, 10], [2, 3]]) == [[1, 10]]
    assert fusionner([[2, 5], [2, 3]]) == [[2, 5]]
    # nombres négatifs
    assert fusionner([[-5, -1], [-2, 2]]) == [[-5, 2]]
    # l'entrée n'est pas modifiée
    creneaux = [[1, 3], [2, 6]]
    fusionner(creneaux)
    assert creneaux == [[1, 3], [2, 6]]
    print("Tous les tests passent")