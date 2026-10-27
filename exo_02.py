"""
Exercice 2 : compression de chaîne (facile, 20 min)

Écris deux fonctions :

compresser(s: str) -> str : "aaabcc" donne "a3b1c2".
decompresser(s: str) -> str : "a3b1c2" donne "aaabcc".

Attention, les nombres peuvent avoir plusieurs chiffres : "x12" donne douze x.
Vérifie que decompresser(compresser(s)) == s pour plusieurs chaînes, y compris la chaîne vide.
"""

"""
def compresser(s:str) -> str:
    if not s:
        return ""

    index, letter, count = 1, s[0], 1
    ans = ""
    while index != len(s):
        if letter == s[index]:
            count += 1
        else:
            ans += f"{letter}{count}"
            letter = s[index]
            count = 1
        index += 1

    ans += f"{s[-1]}{count}"
    return ans

def decompresser(s:str) -> str:
    if not s:
        return ""

    index, letter, digit = 1, s[0], 0
    ans = ""
    while index != len(s):
        if s[index].isalpha():
            ans += letter * digit
            digit = 0
            letter = s[index]
        else:
            digit = digit * 10 + int(s[index])

        index += 1

    ans += letter * digit
    return ans

if __name__ == "__main__":
    assert compresser("aaabcc") == "a3b1c2"
    assert decompresser("a3b1c2") == "aaabcc"
    assert decompresser(compresser("aaabcc")) == "aaabcc"
    print("Tous les tests sont passés")
"""

"""
CORRECTION
"""

def compresser(s: str) -> str:
    """Compresse s en codage par plages. Hypothèse : s ne contient pas de chiffres."""
    if not s:
        return ""
    morceaux = []
    courant, compte = s[0], 1
    for char in s[1:]:
        if char == courant:
            compte += 1
        else:
            morceaux.append(f"{courant}{compte}")
            courant, compte = char, 1
    morceaux.append(f"{courant}{compte}")
    return "".join(morceaux)


def decompresser(s: str) -> str:
    morceaux = []
    caractere, nombre = None, 0
    for char in s:
        if char.isdigit():
            if caractere is None:
                raise ValueError(f"Format invalide : {s!r} commence par un chiffre")
            nombre = nombre * 10 + int(char)
        else:
            if caractere is not None:
                morceaux.append(caractere * nombre)
            caractere, nombre = char, 0
    if caractere is not None:
        morceaux.append(caractere * nombre)
    return "".join(morceaux)


if __name__ == "__main__":
    assert compresser("aaabcc") == "a3b1c2"
    assert decompresser("a3b1c2") == "aaabcc"
    assert compresser("") == "" and decompresser("") == ""
    assert decompresser("x12") == "x" * 12
    assert compresser("x" * 12) == "x12"
    for texte in ["", "a", "aaabcc", "a b!!", "abc", "zzzzzzzzzzzzzzz"]:
        assert decompresser(compresser(texte)) == texte, texte
    print("Tous les tests passent")