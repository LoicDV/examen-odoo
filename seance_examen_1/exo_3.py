def intersection(tab: list[str]) -> str:
    # Démarche :
    # 1. transformer les données en list[str]
    # 2. utiliser intersection des sets
    # Cas limites :
    # liste vide
    if len(tab[0]) == 0 or len(tab[1]) == 0:
        return "false"
    liste_1 = set(tab[0].split(", ")) # format des données
    liste_2 = set(tab[1].split(", "))

    ans = ",".join(sorted(liste_1.intersection(liste_2), key=lambda x : int(x)))
    return ans if ans else "false"

if __name__ == "__main__":
    test1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    test2 = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
    test3 = ["2, 5", "3, 7"]

    assert intersection(test1) == "1,4,13"
    assert intersection(test2) == "1,9,10"
    assert intersection(test3) == "false"
    print("Tous les tests sont passés")