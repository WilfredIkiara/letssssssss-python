import random
#rock paper scissors game
print("WELCOME TO ROCK PAPER SCISSORS... Are you ready to play")
ties = 0
wins = 0
losses = 0
trials = 0

options =["ROCK","PAPER","SCISSORS","rock","paper","scissors"]

while True:
  
  rando=int(random.randrange(0, 99))

  if rando < 33:
    pc_choice = "ROCK"
  elif rando < 66:
    pc_choice = "PAPER"
  else:
    pc_choice = "SCISSORS"
  


  user_choice = input("Pick your saviour!!\nRock .Paper .Sciccors\n q to quit")
  
  if user_choice.upper() == "Q":
    break
  elif user_choice not in options:
    continue
  else:
    pass
  
  print("pc choice is " +pc_choice+" your choice was "+user_choice  )   

  if pc_choice == user_choice:
    ties += 1
    print("You tied with the computer")
  elif user_choice == "ROCK"or"rock" and pc_choice == "PAPER":
    losses += 1
    print("you lost")
  elif user_choice.upper() == "ROCK"or"rock" and pc_choice == "SCISSORS":
    wins += 1
    print("you won")
  elif user_choice.upper() == "PAPER"or"paper" and pc_choice == "SCISSORS":
    losses += 1
    print("you lost")
  elif user_choice.upper() == "PAPER"or"paper" and pc_choice == "ROCK":
    wins += 1
    print("you won")
  elif user_choice.upper() == "SCISSORS"or"scissors" and pc_choice == "ROCK":
    losses += 1
    print("you lost")
  elif user_choice.upper() == "SCISSORS"or"scissors" and pc_choice == "PAPER":
    wins += 1
    print("you won")
  else:
    print("you are entering the wrong spell")
  
  #print("you have "+int(wins)+"wins and "+int(losses)+" losses " +int(ties)+ "ties in "+int(trials)+" trials")
  print(f"You ended with {wins} wins, \n{losses} losses,\n {ties} ties,\n in {trials} trials")
  trials += 1

print(f"You ended with {wins} wins, \n{losses} losses,\n {ties} ties,\n in {trials} trials")
#print("you have "+int(wins)+"wins and "+int(losses)+" losses " +int(ties)+ "ties in "+int(trials)+" trials")
print("Good bye")
