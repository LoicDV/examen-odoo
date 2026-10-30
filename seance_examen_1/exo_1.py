def mot_le_plus_long(phrase: str) -> str:
    # Démarche :
    # 1. Nettoyer la phrase
    # 2. trouver le plus long avec split(" ")
    # Cas limites :
    #   Toujours un mot donc pas de soucis, si meme longueur le premier retourné
    new_phrase = "".join(filter(lambda x : x.isdigit() or x.isalpha() or x == " ", phrase))
    list_mots = new_phrase.split(" ")
    best, leng = list_mots[0], len(list_mots[0])
    for mot in list_mots[1:]:
        if leng < len(mot):
            best = mot
            leng = len(mot)

    return best


if __name__ == "__main__":
    test1 = "le chat&!! dort"
    test2 = "Python est génial !!!"
    test3 = "a bb ccc"

    assert mot_le_plus_long(test1) == "chat"
    assert mot_le_plus_long(test2) == "Python"
    assert mot_le_plus_long(test3) == "ccc"
    print("Tous les tests sont passés")