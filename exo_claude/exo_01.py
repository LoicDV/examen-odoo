"""
Exercice 1 : balises HTML équilibrées (facile, 20 min)

Écris verifier_html(s: str) -> bool | str.

Si toutes les balises sont correctement ouvertes, fermées et imbriquées, renvoie True.
Sinon, renvoie le nom de la première balise fautive.
Les balises autofermantes comme <br/> sont valides seules.
python
verifier_html("<div><b>texte</b></div>")    # True
verifier_html("<div><b>texte</div></b>")    # "b"
verifier_html("<p>a<br/>b</p>")             # True
verifier_html("<div><i>x</i>")              # "div"


def verifier_html(s:str) -> bool | str:
    list_str = decompose(s)
    if len(list_str) == 0:
        return True

    dequeue = []
    for balise in list_str:
        if balise != "br/":
            if not("/" in balise):
                dequeue.append(balise)
            else:
                if len(dequeue) == 0:
                    return balise[1:]

                first_balise = dequeue.pop()
                if first_balise != balise[1:]:
                    return first_balise

    if len(dequeue) != 0:
        return dequeue[-1]
    return True

def decompose(s:str) -> list[str]:
    ans = []
    start = 0
    for i, char in enumerate(s):
        if char == "<":
            start = i+1
        elif char == ">":
            ans.append(s[start:i])
    return ans


if __name__ == "__main__":
    print(verifier_html("<div><b>texte</b></div>"))    # True
    print(verifier_html("<div><b>texte</div></b>"))    # "b"
    print(verifier_html("<p>a<br/>b</p>"))             # True
    print(verifier_html("<div><i>x</i>"))              # "div
"""

"""
CORRECTION
"""

def extraire_balises(s: str) -> list[str]:
    balises = []
    debut = -1
    for i, char in enumerate(s):
        if char == "<":
            debut = i + 1
        elif char == ">" and debut != -1:
            contenu = s[debut:i].strip()
            if contenu:
                balises.append(contenu.split()[0])  # ignore les attributs
            debut = -1
    return balises


def verifier_html(s: str) -> bool | str:
    pile = []
    for balise in extraire_balises(s):
        if balise.endswith("/"):          # autofermante : <br/>, <img/>
            continue
        if balise.startswith("/"):        # fermante
            nom = balise[1:]
            if not pile:
                return nom
            ouverte = pile.pop()
            if ouverte != nom:
                return ouverte
        else:                             # ouvrante
            pile.append(balise)
    return pile[-1] if pile else True


if __name__ == "__main__":
    assert verifier_html("<div><b>texte</b></div>") is True
    assert verifier_html("<div><b>texte</div></b>") == "b"
    assert verifier_html("<p>a<br/>b</p>") is True
    assert verifier_html("<div><i>x</i>") == "div"
    # cas supplémentaires
    assert verifier_html("") is True
    assert verifier_html("</div>") == "div"
    assert verifier_html("<p><img/></p>") is True
    assert verifier_html('<div class="x">a</div>') is True
    assert verifier_html("a > b") is True
    print("Tous les tests passent")