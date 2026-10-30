def spirale(matrice: list[list[int]]) -> list[int]:
    # Démarche :
    # 1. Faire haut, droite, bas, gauche pour revenir au centre
    # 2. Continuer tant que différent 0, 1, 2 cas de base
    # Cas limites :
    #   Tous les cas qui sont des cas de base avec les différences de matrice
    if len(matrice) == 0:
        return []
    if len(matrice) == 1:
        return matrice[0]
    if len(matrice[0]) == 0:
        return []
    if len(matrice[0]) == 1:
        return [row[0] for row in matrice]

    # TOP
    ans = matrice[0]
    # RIGHT
    ans += [row[-1] for row in matrice[1:len(matrice)-1]]
    # BOT
    ans += matrice[-1][::-1]
    # LEFT
    ans += [row[0] for row in matrice[1:len(matrice)-1]]
    new_matrice = [row[1:len(row)-1] for row in matrice[1:len(matrice)-1]]
    return ans + spirale(new_matrice)

if __name__ == "__main__":
    test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    test3 = [[1, 2], [3, 4]]

    assert spirale(test1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spirale(test2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spirale(test3) == [1, 2, 4, 3]
    print("Tous les tests sont passés")