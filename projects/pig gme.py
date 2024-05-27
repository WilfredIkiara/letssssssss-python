import random

def roll():
  min_value= 1
  max_value = 6
  roll = random.randint(min_value, max_value)
  return roll
'''
value = roll()
print(value)
'''
while True:
  players = input("Enter the number of players(2-4):")
  if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Must be between 2 - 4 players.")
  else:
    print("Invalid input. Please try again.")

print("Number of players:", players)

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
  for player_idx in range(players):
    print("Player", player_idx + 1, " turn has just started")
    current_score = 0
    should_roll = input("Would you like to roll (y)? ")
    if should_roll.lower() != "y":
      continue

    while True:
      value = roll()
      if value == 1:
        print("You rolled a 1! Turn done!")
        current_score = 0
        break
      else:
        current_score += value
        print("You rolled a:", value)
        print("Your current score is:", current_score)
        roll_again = input("Roll again (y/n)? ")
        if roll_again.lower() != "y":
          break

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])

print("Game over!")
