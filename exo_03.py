"""
Exercice 3 : mots les plus fréquents (facile-moyen, 25 min)

Écris top_mots(texte: str, k: int) -> list[tuple[str, int]], qui renvoie les k
mots les plus fréquents avec leur nombre d’occurrences.

Ignore la casse et la ponctuation ("Odoo," et "odoo" sont le même mot).
En cas d’égalité, trie par ordre alphabétique.

top_mots("Le chat et le chien. Le chat dort !", 2) # [("le", 3), ("chat", 2)]
"""

"""
def top_mots(texte:str, k:int) -> list[str, int]:
    # Renvoie les k plus grandes occurrences de la chaine de caractères texte. Si
    # plusieurs possibilités parmi les k premiers, on prend dans l'ordre
    # alphabétique.

    # Args:
    #     texte (str): Chaine de caractère à analyser
    #     k (int): Le nombre de mots à renvoyer

    # Returns:
    #     list[str, int]: Liste des mots récupérés avec leur occurrences

    if not texte:
        return []

    list_str = list(filter(lambda x : x != "", map(lambda x : x.strip(",?;.:/-()! '\""), texte.split())))
    list_str_lower = list(map(lambda x : x.lower(), list_str))
    dict_occ = {j : list_str_lower.count(j) for j in set(list_str_lower)}
    sort_dict_occ = sorted(dict_occ.items(), key=lambda item: (-item[1], item[0]))

    ans = []
    for i in range(min(k, len(sort_dict_occ))):
        ans.append(sort_dict_occ[i])

    return ans

if __name__ == "__main__":
    assert top_mots("Le chat et le chien. Le chat dort !", 2) == [("le", 3), ("chat", 2)]
    print("Tous les tests sont passés")
"""

"""
CORRECTION
"""

import string

PONCTUATION = string.punctuation + "«»…"


def top_mots(texte: str, k: int) -> list[tuple[str, int]]:
    """Renvoie les k mots les plus fréquents de texte avec leur nombre d'occurrences.

    La casse et la ponctuation en bordure de mot sont ignorées.
    Les ex aequo sont départagés par ordre alphabétique.
    """
    if k <= 0:
        return []

    compteur: dict[str, int] = {}
    for brut in texte.split():
        mot = brut.strip(PONCTUATION).lower()
        if mot:
            compteur[mot] = compteur.get(mot, 0) + 1

    tries = sorted(compteur.items(), key=lambda item: (-item[1], item[0]))
    return tries[:k]


if __name__ == "__main__":
    phrase = "Le chat et le chien. Le chat dort !"
    assert top_mots(phrase, 2) == [("le", 3), ("chat", 2)]
    # départage alphabétique
    assert top_mots(phrase, 5) == [("le", 3), ("chat", 2), ("chien", 1), ("dort", 1), ("et", 1)]
    # k plus grand que le nombre de mots
    assert top_mots("a b", 10) == [("a", 1), ("b", 1)]
    # vide, k nul, ponctuation isolée
    assert top_mots("", 3) == []
    assert top_mots("a", 0) == []
    assert top_mots("! ? ...", 3) == []
    # casse, ponctuation et retour à la ligne
    assert top_mots("Odoo,\nodoo ODOO!", 1) == [("odoo", 3)]
    print("Tous les tests passent")