#a append
employee_file = open("employee.txt", "a")
employee_file.write("Toby - Human Recouses")
print(employee_file.read())
employee_file.close()