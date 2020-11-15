#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordList = []
passwordStr = ""
password = ""

for i in range(0, nr_letters):
  rando = random.randint(0, len(letters) - 1)
  passwordList.append(letters[rando])
# Angela Yu uses this 👇 approach:
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

for i in range(0, nr_symbols):
  rando = random.randint(0, len(symbols) - 1)
  # passwordList.append(symbols[rando])
  passwordList.append(random.choice(symbols)) # Angela Yu's approach

for i in range(0, nr_numbers):
  # rando = random.randint(0, len(numbers) - 1)
  # passwordList.append(numbers[rando])
  passwordList.append(random.choice(numbers)) # Angela Yu's approach

#print(f"passwordList (pre-shuffle): {passwordList}")
random.shuffle(passwordList)
password = passwordStr.join(passwordList)
print(password)