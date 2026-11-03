userDict = {"name": "Alice", "age": 30, "city": "New York"}
# Accessing elements in a dictionary
user_name = userDict["name"]  # Accessing the value associated with the key "name"
user_age = userDict["age"]  # Accessing the value associated with the key "age"
print(f"\nUser Name: {user_name}")
print(f"User Age: {user_age}\n")

print(f"Keys: {list(userDict.keys())}")  # Printing the entire dictionary
print(f"Values: {list(userDict.values())}")  # Printing the values of the dictionary
print(f"Items: {list(userDict.items())}\n")  # Printing the key-value pairs of the dictionary

complexDict = {"name": "Bob", "permissions": ["read", "write", "delete", "execute"]}
print(f"Permissions: {complexDict['permissions']}")  # Accessing the value associated with the key "permissions"
print(f"First Permission: {complexDict['permissions'][0]}\n")  # Accessing the first permission in the list