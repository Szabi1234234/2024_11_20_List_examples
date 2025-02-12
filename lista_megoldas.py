import random


numbers = [random.randint(-60, 100) for _ in range(50)]
print(numbers)

#1.

#2.
"""last_index_div_5_7 = None
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 or numbers[i] % 7 == 0:
        last_index_div_5_7 = i
print(last_index_div_5_7)
"""
#3
"""
last_index_div_5_7 = None
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 or numbers[i] % 7 == 0:
        last_index_div_3_7 = i
        break
print(last_index_div_3_7)"""
#4.
all_negative = True
for num in numbers:
    if num >= 0:
        all_negative = False
        break
print(all_negative)