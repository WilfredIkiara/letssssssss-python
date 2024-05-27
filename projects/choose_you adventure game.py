name = input("Type your name")
print("welcome", name, "to the adventure of your life")
answer = input("You are on a dark road it has come to an end, you can go left or right, which road will you take type left or right\n").lower()

if answer == "left":
  answer = input("You come to a river and you can walk around it or swim across, tyooe walk to walk, and swim to swim across\n").lower()
  if answer =="swim":
    print("You swam across and were eaten by an Aligator ,you lose ")
  elif answer == "walk":
    print("you walked for many miles , ran out of water and died, you lost the game")
  else:
    print("Not a valid option, you lose. ")
elif answer=="right":
  answer = input("you come to a bridge it looks wabbly do you want to cross it or head back, type cross or  back").lower()

  if answer == "back":
    print("you head back")
  elif answer == "cross":
    answer= input("you meet an old personn do you speak to him. yes or no").lower()
    if answer == "yes":
      answer =input("The stranger offers to take you to his hut, Do you go or you dont, answer yes or No")
      if answer == "yes":
        print("you won the first level of the game congratulations wait for the next chapter of the game to be released")
      elif answer =="no":
        print("you lost the game never even had a chance to win to begin with, where is the spirit of adventure??")
      else:
        print("Not a valid option, you lose. ")
    elif answer == "no":
      print("The old man got offended and stopped your heart ... you lost the game")
    else:
      print("Not a valid option, you lose. ")
  else:
    print("Not a valid option, you lose. ")
else:
  print("Not a valid option, you lose. ")