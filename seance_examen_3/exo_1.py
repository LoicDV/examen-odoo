def rotation(nombres: list[int], k: int) -> list[int]:
    # Démarche :
    # 1. prendre les nombres de fins pour les remettre au début
    # Cas limites :
    #   si k est plus grand que len(nombres) : %
    if not nombres:
        return []
    return nombres[len(nombres)-k%len(nombres):] + nombres[:len(nombres)-k%len(nombres)]


if __name__ == "__main__":
    test1 = [1, 2, 3, 4, 5], 2
    test2 = [1, 2, 3], 4
    test3 = [1, 2, 3], 0

    assert rotation(*test1) == [4, 5, 1, 2, 3]
    assert rotation(*test2) == [3, 1, 2]
    assert rotation(*test3) == [1, 2, 3]
    print("Tous les tests sont passés")