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

import random


user_score = 0
computer_score = 0
user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissor : "))
options = [rock, paper, scissors]
if user_choice > 2:
    print(f"Wrong Input. You lose. Score : {user_score}")
else:
    print("You Choose :" + options[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer Choose :" + options[computer_choice])

    if user_choice == computer_choice:
        user_score+= user_score
        computer_score+=computer_score
        print(f"Its a DRAW. Your Score = {user_score} and Computer Score = {computer_score}")
    elif user_choice == 2 and computer_choice == 0:
        user_score += user_score
        computer_score += 10
        print(f"You Lose ! Your score : {user_score} and Computer Score : {computer_score}")
    elif user_choice == 0 and computer_choice == 2:
        user_score += 10
        computer_score += computer_score
        print(f"You Won ! Your score : {user_score} and Computer Score : {computer_score}")
    elif user_choice > computer_choice:
        user_score += 10
        computer_score += computer_score
        print(f"You Win! Your score : {user_score} and Computer Score : {computer_score}")
    elif computer_choice > user_choice:
        user_score += user_score
        computer_score += 10
        print(f"You Lose ! Your score : {user_score} and Computer Score : {computer_score}")
