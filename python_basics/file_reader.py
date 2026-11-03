customer_file = input("Enter the name of the customer file: ")
file_path = open(customer_file, 'r')

for line in file_path.readlines():
    print(line.strip())

file_path.close()

# >>> f = open("networknuts.txt","w") # Opening the file in write mode. If the file does not exist, it will be created. If it exists, it will be overwritten.
# >>> f.write("Welcome to NetworkNuts GenAI course")
# 35
# >>> f.write("Welcome to NetworkNuts GenAI course")
# 35
# >>> f.close()
# >>> f = open("networknuts.txt","w")
# >>> f.write("Welcome to NetworkNuts GenAI course\n")
# 36
# >>> f.close()
# >>> f = open("networknuts.txt","a") # Appending the file. 
# >>> f.write("This course is meant for 23 classes starting October 2026\n")
# 58
# >>> f.close()
# >>>