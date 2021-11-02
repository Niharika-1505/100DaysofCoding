import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choiceImage = [rock, paper, scissors]

myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = random.randint(0, 2)
print("You chose\n" + choiceImage[myChoice])
print("Computer chose\n" + choiceImage[computerChoice])

if myChoice == computerChoice:
    print("Its a Tie 😁")
else:
    if myChoice == 0:
        if computerChoice == 1:
            print("Computer Won 😭")
        else:
            print("You win 😁")
    elif myChoice == 1:
        if computerChoice == 0:
            print("You win 😁")
        else:
            print("Computer Won 😭")
    else:
        if computerChoice == 0:
            print("Computer Won 😭")
        else:
            print("You win 😁")
