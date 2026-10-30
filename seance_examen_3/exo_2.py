def romain_vers_entier(s: str) -> int:
    # Démarche :
    # 1. partir du plus grand vers le plus petit
    # Cas limites :
    #   attention au 4-9
    ans, flag = 0, False
    for i, char in enumerate(s):
        if flag:
            flag = False
            continue
        if char == "M":
            ans += 1000
        elif char == "D":
            ans += 500
        elif char == "C":
            if i+1 < len(s) and s[i+1] == "M":
                flag = True
                ans += 900
            elif i+1 < len(s) and s[i+1] == "D":
                flag = True
                ans += 400
            else:
                ans += 100
        elif char == "L":
            ans += 50
        elif char == "X":
            if i+1 < len(s) and s[i+1] == "C":
                flag = True
                ans += 90
            elif i+1 < len(s) and s[i+1] == "L":
                flag = True
                ans += 40
            else:
                ans += 10
        elif char == "V":
            ans += 5
        else:
            if i+1 < len(s) and s[i+1] == "X":
                flag = True
                ans += 9
            elif i+1 < len(s) and s[i+1] == "V":
                flag = True
                ans += 4
            else:
                ans += 1
    return ans


if __name__ == "__main__":
    test1 = "III"
    test2 = "LVIII"
    test3 = "MCMXCIV"

    assert romain_vers_entier(test1) == 3
    assert romain_vers_entier(test2) == 58
    assert romain_vers_entier(test3) == 1994
    print("Tous les tests sont passés")