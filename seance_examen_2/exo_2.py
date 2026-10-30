def convertir_minutes(n: int) -> str:
    # Démarche :
    # 1. convertir avec % 60 et // 60
    # 2.
    # Cas limites :
    # miniutes inférieur stricte à 10
    heures = n // 60
    minutes = n % 60 if n % 60 >= 10 else "0" + str(n % 60)
    return f"{heures}h{minutes}"


if __name__ == "__main__":
    test1 = 125
    test2 = 45
    test3 = 600

    assert convertir_minutes(test1) == "2h05"
    assert convertir_minutes(test2) == "0h45"
    assert convertir_minutes(test3) == "10h00"
    print("Tous les tests sont passés")