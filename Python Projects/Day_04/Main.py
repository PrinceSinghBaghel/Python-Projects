import random
print("Welcome to Pypassword Generator!")
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','?']


letter_in=int(input("How many letters would you like in your password ?\n"))
symbols_in=int(input("How many symbols would you like ?\n"))
numbers_in=int(input("How many numbers would you like ?\n"))

#Easy Level
password=""

for char in range(1,letter_in+1):
    random1=random.choice(letter)
    password=password+random1

for char in range(1,symbols_in+1):
    random2=random.choice(symbols)
    password=password+random2

for char in range(1,numbers_in+1):
    random3=random.choice(numbers)
    password=password+random3

final_password=""
for char in range(1,letter_in+symbols_in+numbers_in+1):
    random4=random.choice(password)
    final_password+=random4

print(f"Here is your password : {final_password}")