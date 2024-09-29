print("Welcome to the Rack Paper Scissor Game")

rock = '''
    _______
----'  ____)
      (_____)
      (_______)
      (______)
----,_(____)
      '''
paper = '''
    _______
---'   ____)________
          ___________)
          _______________)
         ____________)
---.______________)
'''

scissors = '''
    _______
---'   ____)____
          __________)
       ___________)
      (____)
---.__(___)
'''


choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print("Your Choice")
games_img=[rock, paper, scissors]

if(choice>2 and choice<0):
    breakpoint()
    print("Invalid")
else:
    print(games_img[choice])


# if(choice==0):
#     print(rock)
# elif(choice==1):
#     print(paper)
# elif(choice==2):
#     print(scissors)
# else:
#     breakpoint()
#     print("Wrong choice")

import random

choice_number=random.randint(0,2)
print(f"Computer Choice {choice_number}")
print(games_img[choice_number])
# if(choice_number==0):
#     print(rock)
# elif(choice_number==1):
#     print(paper)
# else:
#     print(scissors)

if(choice==choice_number):
    print("Score Tied")
elif(choice==0 and choice_number==1):
    print("Computer Wins")
elif(choice==0 and choice_number==2):
    print("You wins")
elif(choice==1 and choice_number==2):
    print("Computer wins")
elif(choice==1 and choice_number==0):
    print("You wins")
elif(choice==2 and choice_number==1):
    print("You wins")
else:
    print("Computer wins")
