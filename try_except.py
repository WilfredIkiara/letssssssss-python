#catching errors

number =int(input("Enter a number"))
print(number)

#lets say you dont enter a number
#what if we want to handle errors
#instead of letting the program crash

try:
  value = 10/ 0
  number =int(input("Enter a number: "))
  print(number)
except ZeroDivisionError as err:
  print(err)
except ValueError as err:
  print(err)
#to protect the program