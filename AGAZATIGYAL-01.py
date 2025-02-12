haromatlag = []

def oszthato(szam):
    
    if szam % 7 == 0 and szam % 3 != 0:
        haromatlag.append(szam)
        return True
    else:
        return False

oszthato(7)
oszthato(14)
oszthato(28)
print(haromatlag )

def atlag(szamok):
    osszeg = 0
    # for szam in szamok:
    #     osszeg += szam
    osszeg = sum(szamok)

    
    print(osszeg)
    hany_db_szam = len(szamok)
    print(hany_db_szam)
    atlag = osszeg / hany_db_szam
    print(atlag)

atlag(haromatlag)