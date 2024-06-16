# List - Shopping list
# Milk, break, butter etc
# adding itme
# Remove item
# Update item
# View Item
# Exit

shopping_list = ["milk", "break", "butter", "Curd"]
print(shopping_list)
print(len(shopping_list))
print((shopping_list[0]))
print((shopping_list[-1]))

shopping_list.append("Vegetables") # Add the item in the end of the list
print(shopping_list)

shopping_list.insert(2,"Apples") # Add the item in the specific index
print(shopping_list)

shopping_list.extend(["Chips","Salt"]) # Add multiple items in the end of the list

shopping_list.remove("break") # Remove the item from the list

shopping_list.reverse() # Reverse the list
print(shopping_list)

shopping_list.pop() # Remove the last item from the list
print(shopping_list)
shopping_list.sort() # Sort the list in alphabetical order
print(shopping_list)

shopping_list[2] = "Oranges" # Update the item in the list
print(shopping_list)

mylist = [1,2,3.0,True,"Veeresh"]
print(mylist)
print(type(mylist))

