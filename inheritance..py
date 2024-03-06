
'''
chef_file = open("chinesechef.py","w" )
chef_file.write("class Chef:")
chef_file.close()
'''
from chinesechef import chinesechef
from chef import Chef

myChef=Chef()
myChef.make_special_dish()

myChineseChef = chinesechef()
myChineseChef.make_special_dish()