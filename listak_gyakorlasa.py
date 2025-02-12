"""Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát! 
1. Mennyi a sorozatban található számok szorzata? 
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét! 
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét! 
4. Igaz-e, hogy minden szám negatív? 
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? 
6. Hány 18-cal osztható szám található a sorozatban? 
7. Mennyi a sorozatban található egyik legkisebb szám indexe? 
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét! 
9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?"""

#1.
#import random

#random_numbers = [random.randint(-60, 100) for _ in range(50)]

#print("1. feladat Generált véletlen számok:", random_numbers)
"""
2.
import random
import math

random_numbers = [random.randint(-60, 100) for _ in range(50)]

product = math.prod(random_numbers)
print("2. feladat")
print("Generált véletlen számok:", random_numbers)
print("A számok szorzata:", product)"""
"""
import random

random_numbers = [random.randint(-60, 100) for _ in range(50)]
print("3. feladat")
print(random_numbers)
last_index = -1
for i in range(len(random_numbers) - 1, -1, -1):
    if random_numbers[i] % 5 == 0 or random_numbers[i] % 7 == 0:
        last_index = i
        break
if last_index != -1:
    print("Az utolso 5 v 7 el oszthato szam indexe:", last_index)
else:
    print("Nincs 5 v 7 el oszthato szam a listaban")
"""
import random

random_numbers = [random.randint(-60, 100) for _ in range(50)]
print("4. feladat")
print(random_numbers)
last_index = -1
for i in range(len(random_numbers) - 1, -1, -1):
    if random_numbers[i] % 3 == 0 or random_numbers[i] % 7 == 0:
        first_index = i
        break
if first_index != 1:
    print("Az utolso 3 v 7 el oszthato szam indexe:", first_index)
else:
    print("Nincs 3 v 7 el oszthato szam a listaban")