is_male = True
is_tall = True

if is_male or is_tall:
  print("you are a tall male")
elif is_male and not is_tall:
  print("you are a short male ") 
elif not (is_male) and is_tall:
  print("you are a tall not male")
else:
  print("you are not a male")