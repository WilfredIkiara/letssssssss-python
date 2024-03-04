#reading information from files in the computer
#name of the file ... what you want to do with the file
#a = append
#r = reading
#w = write
#r+ = read and write
employee_file = open("employee.txt","r")

print(employee_file.read())
print(employee_file.readlines())
#this paces the lines in a array and can be acceessed the same way an array is accessed
employee_file.close()