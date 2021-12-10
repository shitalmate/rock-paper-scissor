import random

def gameWin(comp , you ):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False                        



print("Comp turn : Rock (r), Paper (p) Or Scissor (s)")
print("Comp choose * ")

randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's' 
c = 0
for n in range(5):
    you = input("Your turn : Rock (r), Paper (p) Or Scissor (s)")
    a = gameWin(comp , you)

    print(f"Computer choose {comp}")
    print(f"You choose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!") 
        c = c + 1
    else:
        print("You Lose!")

if(c > 2):
    print("You win the Game")
else:
    print("You Lose the Game")