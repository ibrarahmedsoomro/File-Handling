
# username = input("Enter a  Name: ")
# age = int(input("Enter a  Age: "))
# mobile = int(input("Enter a Mobile Number: ")) 

# with open("data1.txt", "a") as file:
#     file.write(f"Name :{username}\n")
#     file.write(f"Age:{age}\n")
#     file.write(f"Mobile {mobile}\n")
#     file.write("-" * 20 + "\n")
# print("Data Saved Sucessfully")

# with open("data1.txt", "r") as file:
#     lines = file.read()
# print(lines)

# with open("data1.txt", "w") as file:
#     data = file.write()
# print(data)

# with open("data1.txt", "r") as file:
#     print(file.readline())

with open("data1.txt", "r") as file:
    for line in file:
        print(line.strip())


import os

# if os.path.exists("data1.txt"):
#     print("File Exits")
# else:
#     print("File Not Exist")

os.remove("data1.pdf")