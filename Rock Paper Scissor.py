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

#Write your code below this line 👇
import random
choice=int(input("What do you choose? Type 0 for Rock , 1 for Paper, 2 for Scissors"))
num_choice=int(choice)

if num_choice==0:
  print(rock)
elif num_choice==1:
  print(paper)
else:
  print(scissors)
print("Computer chose:\n")
computer= random.randint(0,2)
if computer==0:
  print(rock)
elif computer==1:
  print(paper)
else:
  print(scissors)

if computer==0:
  if num_choice==0:
    print("Draw")
  elif num_choice==1:
    print("Paper beats Rock\n\n You win!")
  elif num_choice==2:
    print("Rock beats Scissors\n\n You lose!")

if computer==1:
  if num_choice==0:
    print("Paper beats Rock\n\n You lose")
  elif num_choice==1:
    print("Draw")
  elif num_choice==2:
    print("Scissors beats Paper\n\n You win!!")

if computer==2:
  if num_choice==0:
    print("Rock beats Scissors\n\nYou win!")
  elif num_choice==1:
    print("Scissors beats Paper\n\n You lose!")
  elif num_choice==2:
    print("Draw")