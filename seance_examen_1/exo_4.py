def identifiant_valide(nom: str) -> str:
    # Démarche :
    # 1. check des regles sinon "false" sans test le reste
    # 2. faire les tests des plus simples en temps vers le plus gourmand
    if 4 > len(nom) or len(nom) > 25:
        return "false"

    if not nom[0].isalpha():
        return "false"

    if nom[-1] == "_":
        return "false"

    check_alpha = set("azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN")
    for char in nom:
        if char not in check_alpha and not char.isdigit() and char != "_":
            return "false"

    return "true"

if __name__ == "__main__":
    test1 = "u__hello_world123"
    test2 = "aa_"
    test3 = "1abc"
    test4 = "café_42"

    assert identifiant_valide(test1) == "true"
    assert identifiant_valide(test2) == "false"
    assert identifiant_valide(test3) == "false"
    assert identifiant_valide(test4) == "false"
    print("Tous les tests sont passés")