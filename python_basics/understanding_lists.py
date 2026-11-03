userList = ["Alice", "Bob", "Charlie", "David", "Eve"]
mixedData = [42, "Hello", 3.14, True, None]

# Accessing elements in a list
first_user = userList[0][0:3]  # Accessing the first element
last_user = userList[4]  # Accessing the last element
print(f"\nFirst user: {first_user}")
print(f"Last user: {last_user}\n")

userList.append("Frank")  # Adding a new user to the list
print(f"Updated user list: {userList}\n")

userList.pop()  # Removing the last user from the list
print(f"User list after removing the last user: {userList}\n")

nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a nested list
first_nested_element = nestedList[1][1]  # Accessing the second element of the first nested list
print(f"First nested element: {first_nested_element}\n")

userList[0] = "Alicia"  # Modifying the first element of the list
print(f"Modified user list: {userList}\n")