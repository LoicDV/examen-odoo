def type_suite(nombres):
    ecart = nombres[1] - nombres[0]
    if all(nombres[i] - nombres[i - 1] == ecart for i in range(2, len(nombres))):
        return "arithmetique"
    # rapport constant : n[i] / n[i-1] == n[1] / n[0], écrit sans division
    a, b = nombres[0], nombres[1]
    if all(nombres[i] * a == nombres[i - 1] * b for i in range(2, len(nombres))):
        return "geometrique"
    return "aucune"

if __name__ == "__main__":
    test1 = [2, 4, 6, 8]
    test2 = [2, 6, 18, 54]
    test3 = [1, 2, 4, 7]
    test4 = [343, 147, 63, 27]

    assert type_suite(test1) == "arithmetique"
    assert type_suite(test2) == "geometrique"
    assert type_suite(test3) == "aucune"
    assert type_suite(test4) == "geometrique"
    print("Tous les tests sont passés")