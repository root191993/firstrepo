"""
WorkFlow -- Project
1 - input from user(Rock, Paper, Scissor)
2 - Random choice (Computer choose randomly not conditionaly)
3 - print out the result


Cases:
A- Rock
Rock - Rock -- match tie
Rock - Paper -- Paper win
Rock - Scissor -- Rock win

B - Paper


Paper - Rock --  Paper win
Paper - Scissor -- Scissor win
Paper - Paper -- Paper tie
C - Scissor
Scissor - Scissor -- Match tie
Scissor - Paper -- scissor win
Scissor - Rock -- Rock win
"""
import random

Items = ["Rock", "Paper", "Scissor"]
Users = input("Enter the move: ")
Computer = random.choice(Items)
print(f"User_choice: {Users}, Computer_choice: {Computer}")
if Users == Computer:
    print("Draw")
elif Users == "Rock" :
    if Computer == "Paper":
        print("Rock smashes Scissor, Rock win")
    else:
       print("You lose")

elif Users == "Scissor" :
    if Computer == "Paper":
       print("Scissor cuts Paper, Scissor win")
    else:
     print("you lose")
elif Users == "Paper" :
     if Computer == "Rock":
      print("Paper covers Rock, Paper win")
     else:
      print("you lose")