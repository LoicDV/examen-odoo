def produit_des_autres(nombres: list[int]) -> list[int]:
    # Démarche :
    # 1. Parcourir 2 fois la liste (gauche et droite)
    # 2. donner la valeur dans la liste finale puis prendre celui de l'indice
    ans = [1] * len(nombres)
    pivot = 1
    for i, num in enumerate(nombres):
        ans[i] *= pivot
        pivot *= num
    pivot = 1
    for i in range(len(nombres)-1, -1, -1):
        ans[i] *= pivot
        pivot *= nombres[i]
    return ans

if __name__ == "__main__":
    test1 = [1, 2, 3, 4]
    test2 = [2, 0, 4]
    test3 = [3, 4]

    assert produit_des_autres(test1) == [24, 12, 8, 6]
    assert produit_des_autres(test2) == [0, 8, 0]
    assert produit_des_autres(test3) == [4, 3]
    print("Tous les tests sont passés")