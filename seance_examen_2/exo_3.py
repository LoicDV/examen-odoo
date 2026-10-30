def premier_unique(s: str) -> str:
    # Démarche :
    # 1. faire un dict occurence pour trouver ceux où val = 1
    # 2. parcourir s
    # Cas limites :
    # gérer si tous diff 1
    dict_occ = {k : s.count(k) for k in set(s)}
    for char in s:
        if dict_occ[char] == 1:
            return char
    return "aucun"

if __name__ == "__main__":
    test1 = "abracadabra"
    test2 = "Python"
    test3 = "aabb"

    assert premier_unique(test1) == "c"
    assert premier_unique(test2) == "P"
    assert premier_unique(test3) == "aucun"
    print("Tous les tests sont passés")