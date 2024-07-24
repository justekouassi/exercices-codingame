def Licence(x: str, n: int):
    x = x.split('-')

    somme = int(x[1]) + n
    reste = somme % 999
    x[1] = str(reste)

    reste2 = 0
    reste3 = 0
    reste4 = 0
    somme2 = ord(x[2][1]) + (somme//999)
    while (somme2 > 90):
        somme2 -= 26
        reste2 += 1
    somme3 = ord(x[2][0]) + reste2
    while (somme3 > 90):
        somme3 -= 26
        reste3 += 1
    x[2] = chr(somme3 + reste3) + chr(somme2)
    somme4 = somme3 + reste3
    # print(somme4)
    # while (somme4 > 90):
    #     somme4 -= 26
    #     reste4 += 1
    # x[0] = chr(ord(x[0][0])) + chr( somme4 )

    print(f"{x[0]}-{x[1].rjust(3, '0')}-{x[2]}")


Licence("AB-123-CD", 5)  # AB-128-CD
Licence("AZ-566-QS", 100)  # AZ-666-QS
Licence("BN-999-GH", 1)  # BN-001-GI
Licence("CG-007-CG", 10000)  # CG-017-CQ
Licence("IO-010-OI", 100000)  # IO-110-SE
Licence("QS-456-DF", 1000000)  # QT-457-PS
Licence("ER-963-DF", 87654321)  # JQ-027-XY
