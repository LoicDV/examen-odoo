def lettres_encadrees(s: str) -> str:
    # Démarche :
    # 1. parcourir la chaine pour trouver une lettre
    # 2. vérifier si il y a bien un + avant et apres (return true a la fin)
    # Cas limites :
    # chaine vide
    if len(s) == 0:
        return "true"

    for i, char in enumerate(s):
        if char.isalpha():
            if i in (0, len(s)-1):
                return "false"

            if s[i-1] != "+" or s[i+1] != "+":
                return "false"

    return "true"


if __name__ == "__main__":
    test1 = "+d+=+s+"
    test2 = "f++d+"
    test3 = "++a+b+"

    assert lettres_encadrees(test1) == "true"
    assert lettres_encadrees(test2) == "false"
    assert lettres_encadrees(test3) == "true"
    print("Tous les tests sont passés")