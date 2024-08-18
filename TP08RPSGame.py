# import random module

import random

# print multiline instruction


print("Rock Paper Scissor Game by Team Achievers!!")

print("""
The Rules of the game are :\n
Rock vs Paper -> Paper wins \n
Rock vs Scissors -> Rock wins \n
Paper vs Scissors -> Scissor wins \n
""")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user

    choice = int(input("Enter your choice (1,2,3):"))

    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value

    # looping until user enter invalid input
   
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

        # initialize value of choice_name variable
    # corresponding to the choice value
  
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # print user choice
   
    print('Your Choice is \n', choice_name)
    print('The Turn of AI now....')

    # AI will randomly choose any number
    # among 1 , 2 and 3. Using randint method
    # of random module
   
    AI_choice = random.randint(1, 3)

    # looping until AI_choice value
    # is equal to the choice value
   
    while AI_choice == choice:
        AI_choice = random.randint(1, 3)

     # initialize value of AI_choice_name
    
    # variable corresponding to the choice value
 
    if AI_choice == 1:
        AI_choice_name = 'RocK'
    elif AI_choice == 2:
        AI_choice_name = 'Paper'
    else:
        AI_choice_name = 'Scissors'

    print("AI's choice is \n", AI_choice_name)

    print(choice_name, 'Vs', AI_choice_name)
    
    # we need to check of a draw
   
    if choice == AI_choice:
        print('Its a Draw', end="")
        result = "DRAW"


    # condition for winning
  
    if (choice == 1 and AI_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and AI_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and AI_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and AI_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and AI_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and AI_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'


     # Printing either user or AI wins or draw
    
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== AI wins ==>")
    print("Do you want to play again? (Y/N)")


    # if user input n or N then condition is True
  
    ans = input().lower()
   
    if ans == 'n':
        break


# after coming out of the while loop

# we print thanks for playing
print("thanks for playing")