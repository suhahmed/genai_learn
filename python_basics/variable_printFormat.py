print("Welcome to the World of Gene AI\n")
username = "Suhail"
userid = 101

print ("Method 1: DOT FORMAT - Python2 + Python3")
print("Hi {}. Your UserID is {}.\n".format(username, userid))

print("Method 2: F-STRING - Python3.6+")
print(f"Hi {username}. Your UserID is {userid}.\n")

username = input("Enter your name: ")
if username=="Suhail":
    print(f"Hi {username}. Your UserID is {userid}.\n")
else:
    print(f"Hi {username}. Your UserID is not found.\n")