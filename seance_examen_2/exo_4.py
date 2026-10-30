def type_suite(nombres: list[int]) -> str:
    # Démarche :
    # 1. voir si on est l'un l'autre ou les 2
    # 2. tester sur les suivants
    # Cas limites :
    # Si à la fois arith et geom
    num_1, num_2, num_3 = nombres[0], nombres[1], nombres[2]
    arith, geom = False, False
    if num_1 - num_2 == num_2 - num_3:
        arith = try_arith(nombres[2:], num_1-num_2)

    if 0 not in (num_2, num_3) and num_1 / num_2 == num_2 / num_3:
        geom = try_geom(nombres[2:], num_1/num_2)

    if arith:
        return "arithmetique"
    if geom:
        return "geometrique"
    return "aucune"


def try_arith(nombres:list[int], rapport:int) -> bool:
    for i in range(len(nombres)-1):
        if nombres[i] != nombres[i+1] + rapport:
            return False
    return True

def try_geom(nombres:list[int], rapport:float) -> bool:
    for i in range(len(nombres)-1):
        if nombres[i] != nombres[i+1] * rapport:
            return False
    return True


if __name__ == "__main__":
    test1 = [2, 4, 6, 8]
    test2 = [2, 6, 18, 54]
    test3 = [1, 2, 4, 7]

    assert type_suite(test1) == "arithmetique"
    assert type_suite(test2) == "geometrique"
    assert type_suite(test3) == "aucune"
    print("Tous les tests sont passés")