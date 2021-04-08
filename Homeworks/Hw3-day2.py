import os
clear = lambda: os.system('cls')
username = input("Please Create a Username: ")
password = input("Please Create a Password: ")
print("Your username/password is:", username,"/",password,"\n")
check = input("Are you sure for your username and password?(Y or N) ")
print(check)
while check == "N" or check == "n":
    clear()
    username = input("Please Create a Username: ")
    password = input("Please Create a Password: ")
    print("Your username/password is:", username,"/",password,"\n")
    check = input("Are you sure for your username and password?(Y or N) ")
    if check == "Y" or check == "y":
        break
if check == "Y" or check == "y":
    clear()
    input1 = input("Please enter your username: ")
    while input1 != username:
        input1 = input("Username couldn't found. Please enter a valid username: ")
    if input1 == username:
        clear()
        print("Your username:", input1)
        input2 = input("Please enter your password: ")
        while input2 != password:
            input2 = input("Wrong password, try again: ")
        if input2 == password:
            print ("Congrats, you're in.")

    
