"""
B csoport
Olvassunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?
"""
numbers = []
    
 
while True:
    try:
        num = int(input("Kérem, adjon meg egy egész számot (0 a befejezéshez): "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Kérem, érvényes egész számot adjon meg!")
    
 
print("1. feladat:")
has_between = any(-15 < n < -10 for n in numbers)
print("Volt -10 és -15 közé eső szám:", has_between)

print("2. feladat:")
osztahatok = [n for n in numbers if n % 2 == 0 or n % 5 == 0]
print("2,5-el osztható számok:", osztahatok)

print("3. feladat: ")
nagyobb = [n for n in numbers if n > 20]
print(f"20-nál nagyobb számok:{nagyobb} ")
# felkesz
print("4. feladat: ")
utolsolegkisebb = [n for n in numbers if n > 0]

print(f"mennyi volt a legkisebb beírt pozitív egész szám?{min(utolsolegkisebb)}")

#for i in range(len(numbers)):
    #print(numbers[i])
  #  print(i)

#print(index.legkisebbutolsolegkisebb)




print("5. feladat:")
negative_numbers = [n for n in numbers if n < 0]
if negative_numbers:
    average_of_negatives = sum(negative_numbers) / len(negative_numbers)
    print("A negatív számok átlaga:", average_of_negatives)
else:
    print("nem volt negativ szam")
    