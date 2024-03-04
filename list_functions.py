lucky_numbers = [4, 8, 15, 16, 23, 42]
friends=["Glenn","adrian", "Hilal","Jeff","melly"]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Brian")
friends.insert(1, "Kelly")
friends.remove("kelly")
friends.clear()#clears the list
friends.pop()
print(friends.index("Hilal"))
print(friends.count("Glenn"))
friends.sort()#arranges in alphabetical order
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
friends2 = friends.copy
print(friends2)