def parentheses_equilibrees(s: str) -> str:
    # Démarche :
    # 1. parcourir la chaine pour trouver les ouvrantes et les mettre dans queue
    # 2. si fermante, on retire la derniere mise et on compare
    # Cas limites :
    # s'il reste des éléments dans la queue et check queue si vide
    dict_check = {"(" : ")", "[" : "]", "{" : "}"}
    queue = []

    for char in s:
        if char in ("(", "[", "{"):
            queue.append(char)
        elif char in (")", "]", "}"):
            if not queue:
                return "false"
            checker = dict_check[queue.pop()]
            if checker != char:
                return "false"

    if queue:
       return "false"
    return "true"


if __name__ == "__main__":
    test1 = "(a[b]{c})"
    test2 = "(]"
    test3 = "([)]"
    test4 = "(()"

    assert parentheses_equilibrees(test1) == "true"
    assert parentheses_equilibrees(test2) == "false"
    assert parentheses_equilibrees(test3) == "false"
    assert parentheses_equilibrees(test4) == "false"
    print("Tous les tests sont passés")