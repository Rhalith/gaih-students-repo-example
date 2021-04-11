import os
clear = lambda: os.system('cls')
introduction = "Welcome to the knowledge competition.\nYou have to answer at least 5 questions correctly to be successful.\n\nThere are few rules before beginning:\n1-You should use capital keys for answer.(For example: emir(wrong), Emir(correct))\n2-You can take 3 hint for questions by typing 'H'. You can use them for only once at a question.\n3-You can skip questions by typing 'S', but you cannot go back to answer them!\n4-You can only answer once to each questions." 
number = 0
hint = 0
hintt = 0
ans = 0
question1 = "1- What is the world's best-selling game?"
answer1 = "Minecraft"
hint1 = "This game allows you to make various designs with cubes."
question2 = "2- What is the world's first 3D film?"
answer2 = "Avatar"
hint2 = "Its the name of the last airbender"
question3 = "3- Who's the first person to set foot on the moon?"
answer3 = "Neil Armstrong"
hint3 = "His name is something like N__l A__st___g"
question4 = "4- Who is the inventor of bitcoin.(According to it's whitepaper)"
answer4 = "Satoshi Nakamoto"
hint4 = "His name is something like S__os__ N___moto"
question5 = "5- Who is the founder of Facebook?"
answer5 = "Mark Zuckerberg"
hint5 = "His name is something like M__k Z__ke___rg"
question6 = "6- Who is Turkey's 9th president?"
answer6 = "Süleyman Demirel"
hint6 = "His name is something like Sü____an De____l"
question7 = "7- Who invented the law of gravity?"
answer7 = "Isaac Newton"
hint7 = "His surname is also unit of Force at pyhsic"
question8 = "8- How many millimeters is a meter?"
answer8 = "1000"
hint8 = "1 centimeter is 100 milimetres"
question9 = "9- Who is the Marvel character who lost his life after stopping the Thanos at the end of the movie Endgame?"
answer9 = "Iron Man"
hint9 = "His first name is the same as the name of an element"
question10 = "10- Please solve the equation '6 / 2 * (2+1)'"
answer10 = "10"
hint10 = "Use the transaction Priority"
print(introduction)
input("If you're ready type something and we can start\n")
clear()
print(question1)
while ans != answer1:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint1)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer1:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question2)
hintt = 0
ans = 0
while ans != answer2:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint2)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer2:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question3)
hintt = 0
ans = 0
while ans != answer3:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint3)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer3:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question4)
hintt = 0
ans = 0
while ans != answer4:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint4)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer4:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question5)
hintt = 0
ans = 0
while ans != answer5:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint5)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer5:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question6)
hintt = 0
ans = 0
while ans != answer6:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint6)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer6:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question7)
hintt = 0
ans = 0
while ans != answer7:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint7)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer7:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question8)
hintt = 0
ans = 0
while ans != answer8:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint8)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer8:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question9)
hintt = 0
ans = 0
while ans != answer9:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint9)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer9:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
print(question10)
hintt = 0
ans = 0
while ans != answer10:
    ans = input()
    if ans == "H":
        if hint < 3 and hintt != 1:
            print(hint10)
            hint += 1
            hintt = 1
        else:
            print("You cannot take more hint!")
    elif ans == "S":
        clear()
        print("Okay, You've skipped the question.")
        break
    elif ans == answer10:
        clear()
        print("Congrats. You gave correct answer!")
        number += 1
        break
    else:
        clear()
        print("You've gave wrong answer.")
        break
clear()
if number > 5:
    print("Congrats! You are a successful by giving", number ,"true answers")
else:
    print("Sorry, you need to work hard. You only gave", number ," true answers.")
print("You used", hint ,"hints\n")
input()