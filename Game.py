
import random

def game():
	user = input("Choose Rock , Paper or Scissor : ").lower()
	
	options =["rock","paper","scissor"]
	computer = random.choice(options)
	if user == computer:
		print(f"You choose {user} Computer choose {computer}\nResult is DRAW!")
	elif (user =="rock" and computer =="scissor") or (user =="paper" and computer =="rock") or (user =="scissor" and computer =="paper"):
		print(f"You choose {user} Computer choose {computer}\nResult is YOU WON!")
	else:
		print(f"You choose {user} Computer choose {computer}\nResult is YOU LOST!")
	
game()
user_choice = input("Type 'Exit' to exit the game and 'Go' to continue : ").lower()

while user_choice =="go":
	game()
	user_choice = input("Type 'Exit' to exit the game and 'Go' to continue : ").lower()
	