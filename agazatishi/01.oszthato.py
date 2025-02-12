haromjegyuszamok = []

for szam in range(100, 1000):
    if szam % 7 == 0 and szam % 3 != 0:
        haromjegyuszamok.append(szam)

print(haromjegyuszamok)


def oszthato(szamok):
    osszeg = sum(szamok)
    darab_szamok = len(szamok)
    atlag = osszeg / darab_szamok
    return atlag

print(f"wawawawa {oszthato(haromjegyuszamok)}")
# haromatlag = []

# def oszthato(szam):
    
#     if szam % 7 == 0 and szam % 3 != 0:
#         haromatlag.append(szam)
#         return True
#     else:
#         return False

# oszthato(7)
# oszthato(14)
# oszthato(28)
# print(haromatlag )

# def atlag(szamok):
#     osszeg = 0
#     # for szam in szamok:
#     #     osszeg += szam
#     osszeg = sum(szamok)

    
#     print(osszeg)
#     hany_db_szam = len(szamok)
#     print(hany_db_szam)
#     atlag = osszeg / hany_db_szam
#     print(atlag)

# atlag(haromatlag)