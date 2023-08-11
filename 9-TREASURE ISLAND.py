print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the treasure island.\nYou have arrived at a junction.")
name = input("Type your name to continue.\n")
score = 0
choice = input(f"Type 'LEFT' to go left or type 'RIGHT' to go to the right.Your score is {score}\n").upper()
if choice == "LEFT":
    score+=1
    choice_1 = input(f"{name} arrived near a lake. Type 'WAIT' to wait for the boat or 'SWIM' to swim across the lake. Your score is {score}\n").upper()
    if choice_1 == "WAIT":
        score+=1
        choice_2 = input(f"{name} has arrived at the shore. There are three doors. Yellow, Blue and Red. Which door will you opem ? Your score is {score}\n").upper()
        if choice_2 == "RED":
            score=score
            print(f"{name} entered room full of demons. Game Over. Your score is {score}!")
        elif choice_2 == "BLUE":
            score +=1
            print(f"Congratulations {name}, You have arrived at the treasure. You Win !. Your score is {score}")
        elif choice_2 == "YELLOW":
            score=score
            print(f"{name} slipped in a room full of fire. Game Over ! Your score is {score}")
        else:
            score=0
            print(f"Incorrect Input. Game Score. Your score is {score}")
    elif choice_1 == "SWIM":
        score=score
        print(f"Oh no ! You have been eaten up by shark. You died. Your score is {score}")
elif choice == "RIGHT":
    print(f"You ended up in a cave and eaten up by a lion. Game Over. Your score is {score}")