def somme_chiffres(s: str) -> int:
    # Démarche :
    # 1. Nettoyer pour retirer les lettres
    # 2. utiliser ord pour la conversion
    # Cas limites :
    # chaine vide et si pas de nombre
    filter_s = list(filter(lambda x : x.isdigit(), s)) # [] si vide
    ans = 0
    for num_str in filter_s:
        ans += ord(num_str) - ord('0')
    return ans


if __name__ == "__main__":
    test1 = "a1b2c3"
    test2 = "x9y0z"
    test3 = "abc"

    assert somme_chiffres(test1) == 6
    assert somme_chiffres(test2) == 9
    assert somme_chiffres(test3) == 0
    print("Tous les tests sont passés")