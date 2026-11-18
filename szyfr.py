import math

word = input("Podaj słowo do zaszyfrowania: ")
while not word.isalpha():
    word = input("Niepoprawna wartość. Podaj słowo do zaszyfrowania WYŁĄCZNIE literami: ")

ch1 = int(input("Wybierz liczbę 1 lub 2: "))
while ch1 != 1 and ch1 != 2:
    ch1 = int(input("Niepoprawna wartość. Wybierz liczbę 1 lub 2: "))

ch2 = float(input("Wybierz dowolną liczbę większą od 0: "))
while ch2 <= 0:
    ch2 = float(input("Niepoprawna wartość. Wybierz dowolną liczbę większą od 0: "))

if ch1 == 1:
    result = math.pi * math.sqrt(ch2)

elif ch1 == 2:
    result = math.e * math.sqrt(ch2)

text = str(result)
text = text.partition(".")[2]

coded = ""

for character, digit in zip(word, text):
    add = chr(ord(character) + int(digit))
    coded += add

print(f"Zakodowane słowo: {coded} ")
