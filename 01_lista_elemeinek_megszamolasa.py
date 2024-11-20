"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""
szamok = [5, 8, 12, 15, 22]

hossz = 0
for i in szamok:
    hossz = hossz + 1

    
   # print(szamok[i])
   # i = i + 1
   
print(f"Lista ekemi len ciklussal: {len(szamok)}")

print(f"A lista hossza: {hossz}")