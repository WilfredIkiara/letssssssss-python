print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Lets play :) ")
score = 0
answer = input("What does CPU stad for? ")
if answer.lower() == "central processing unit" :
  print("Correct !!")
  score += 1
else:
  print("Incorrrect !!")

answer = input("What does GPU stad for? ")
if answer.lower() == "graphics processing unit" :
  print("Correct !!")
  score += 1
else:
  print("Incorrrect !!")

answer = input("What does RAM stad for? ")
if answer.lower() == "random acces memoryt" :
  print("Correct !!")
  score += 1
else:
  print("Incorrrect !!")

answer = input("What does PSU stad for? ")
if answer.lower() == "power supply" :
  print("Correct !!")
  score += 1
else:
  print("Incorrrect !!")

print("you got " +str(score)+ " correct questions")

print("you got "+str((score/4)*100)+" %.")