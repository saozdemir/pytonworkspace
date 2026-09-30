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
states = [rock, paper, scissors]
you_win = False
user_choice_index = int(input("What do you choice? Type: \n"
                    "0 for Rock\n"
                    "1 for Paper\n"
                    "2 for Scissors\n"))

computer_choice = random.choice(states)
computer_choice_index = states.index(computer_choice)
if user_choice_index >= 0 and user_choice_index < 3:
    print("Computer Selection: \n" + states[computer_choice_index] + "\n")
    print("Your Selection: " + states[user_choice_index] + "\n")
    if computer_choice_index == 0 and user_choice_index ==2:
        print("You lose!")
    elif user_choice_index ==0 and computer_choice_index ==2:
        print("You win!")
    elif computer_choice_index > user_choice_index:
        print("You lose!")
    elif computer_choice_index < user_choice_index:
        print("You win!")
    elif computer_choice_index == user_choice_index:
        print("It's a draw!")
else:
    print("Wrong selection. Game Over.")