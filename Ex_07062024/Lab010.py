dir = r'C:\namedir\some dir'

print(dir)

first_name = "Veeresh"
last_name = "Basirala"

print(first_name + last_name)
print(first_name + " " + last_name)

print("My name is: " + first_name + " " + last_name)
print(f"{first_name} {last_name}")
print("My name is: {} {}".format(first_name, last_name))

print(id(first_name)) # id --> memory address where it is stored 2543553877056
print(len(last_name))  # length of the string 6

print(first_name.upper())
print(first_name.lower())
print(first_name.find('e'))
count = first_name.count('e')
print(count)

print(first_name[3]) # String index out of range
