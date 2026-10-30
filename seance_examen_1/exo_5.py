def compresser(s: str) -> str:
    # Démarche :
    # 1. prendre la lettre et check combien de fois elle va être suivi
    # 2. ajouter le tout dans une liste puis join
    # Cas limites :
    # chaine vide et insérer la derniere partie
    if not s:
        return ""
    ans = []
    letter, count = s[0], 1
    for char in s[1:]:
        if char == letter:
            count += 1
        else:
            ans.append(f"{count}{letter}")
            letter, count = char, 1
    ans.append(f"{count}{letter}")
    return "".join(ans)


if __name__ == "__main__":
    test1 = "wwwggopp"
    test2 = "aabbcde"
    test3 = "zzzzzzzzzzzz"
    test4 = "abab"

    assert compresser(test1) == "3w2g1o2p"
    assert compresser(test2) == "2a2b1c1d1e"
    assert compresser(test3) == "12z"
    assert compresser(test4) == "1a1b1a1b"
    print("Tous les tests sont passés")