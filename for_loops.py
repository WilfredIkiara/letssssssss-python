friends = ["Jim ", "Karen", "Kelvin" ]
len(friends)
for index in range (5):
  if index == 0:
    print("first iteration")
  else:
    print("not first")

for index in range (len(friends)):
  print(friends[index])

for friend in friends:
  print(friend)