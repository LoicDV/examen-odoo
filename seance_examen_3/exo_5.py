def nb_sous_listes(nombres: list[int], k: int) -> int:
    # Démarche :
    # 1. Calculer la somme courante en la mettant dans un dictionnaire
    # 2. Propager le nombre total dans le dictionnaire
    vues = {0: 1}
    curr = 0
    total = 0
    for x in nombres:
        curr += x
        total += vues.get(curr - k, 0)
        vues[curr] = vues.get(curr, 0) + 1
    return total

if __name__ == "__main__":
    test1 = [1, 1, 1], 2
    test2 = [1, 2, 3], 3
    test3 = [1, -1, 0], 0

    assert nb_sous_listes(*test1) == 2
    assert nb_sous_listes(*test2) == 2
    assert nb_sous_listes(*test3) == 3
    print("Tous les tests sont passés")