word = input("Podaj słowo WYŁĄCZNIE literami: ")
while not word.isalpha():
    word = input("Niepoprawna wartość. Podaj słowo WYŁĄCZNIE literami: ")

key = int(input("Podaj klucz: "))

coded = ""

text = str(key)

for char in word:
    base = ord("A") if char.isupper() else ord("a")
    coded += chr((ord(char) - base + key) % 26 + base)

print(f"Zakodowane słowo: {coded}")