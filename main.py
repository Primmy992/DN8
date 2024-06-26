DN 8.1

mood = str(input("How do you feel?"))

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervus":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Get happier!")
elif mood == "excited":
    print("You just can't hide it?")
elif mood == "relaxed":
    print("Take a deep breath 3 times.")
else:
    print("I don't recognize this mood")

-----------------------------------------------------
DN 8.2 PRIMER 1

import random

guess = int(input("Vnesi število:"))
secretNumber=random.randint(1,10)

while guess != secretNumber:
    print("Nepravilno! Poizkusi znova")
    guess = int(input("Vnesi število:"))
print("Bravo!", guess," je pravilen odgovor!")

-----------------------------------------------------
DN 8.2 PRIMER 2
secret = 5
guess = int(input("Ugani število:"))
pravilno = True
napacno = False


if guess!= secret:
    print(napacno)
else:
    print(pravilno)

-----------------------------------------------------
DN 8.3 PRIMER 1

while 1:
    firstNumber = int(input("Vnesi prvo stevilo:"))
    secondNumber = int(input("Vnesi drugo stevilo:"))
    calc = str(input("Vnesi +, če želiš seštevati, - za odštevanje, * za množenje ali / za deljenje:"))
    match calc:
        case "+":
            print(firstNumber + secondNumber)
        case "-":
            print(firstNumber - secondNumber)
        case "*":
            print(firstNumber * secondNumber)
        case "/":
            division: float = firstNumber / secondNumber
            print(division)
        case _:
            print("Napačen vnos!")
            break
-----------------------------------------------------
DN 8.3 PRIMER 2
firstNumber = int(input("Vnesi prvo stevilo:"))
secondNumber = int(input("Vnesi drugo stevilo:"))
calc = str(input("Vnesi +, če želiš seštevati, - za odštevanje, * za množenje ali / za deljenje:"))


if calc == "+":
    print(firstNumber + secondNumber)
elif calc == "-":
    print(firstNumber - secondNumber)
elif calc == "*":
    print(firstNumber * secondNumber)
elif calc == "/":
    deljenje: float = firstNumber / secondNumber
    print(deljenje)
else:
    print("Napacen vnos!")