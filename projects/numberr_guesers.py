import random 

#random.radrage(start, stop)
#r = random.randrange(5, 11)
#r = random.randint(5, 11)  includes last number
#print(r)
top_of_range = input ("type a number: ")


if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print("please type a number more than zero")
    quit()
  else:
    print("please type a number next time")
random_number = random.randint(0, top_of_range)
int(random_number)
guesses = 0

while True:
  guesses += 1
  user_guess= input("make a guess: ")
  if user_guess.isdigit():
    user_guest = int(user_guess)
  else:
    print("please type anumber next time. ")
    continue

  if user_guess == random_number:
    print("you got it")
    break
  elif user_guess > random_number:
    print("you were above the number")
  else:
    print("You were below the number")

print("you got it in s"+int(guesses)+" guesses")
