

student1 = input("Please enter first student's name: ")
student1_1 = int(float(input("Please enter first student's midterm grade: ")))
student1_2 = int(float(input("Please enter first student's project grade: ")))
student1_3 = int(float(input("Please enter first student's final grade: ")))
while student1_1 < 0 or student1_1 > 100 or student1_2 < 0 or student1_2 > 100 or student1_3 < 0 or student1_3 > 100:
    print("Error! Grades must be between 0 and 100")
    student1_1 = int(float(input("Please enter first student's midterm grade: ")))
    student1_2 = int(float(input("Please enter first student's project grade: ")))
    student1_3 = int(float(input("Please enter first student's final grade: ")))
print()
student2 = input("Please enter second student's name: ")
student2_1 = int(float(input("Please enter second student's midterm grade: ")))
student2_2 = int(float(input("Please enter second student's project grade: ")))
student2_3 = int(float(input("Please enter second student's final grade: ")))
while student2_1 < 0 or student2_1 > 100 or student2_2 < 0 or student2_2 > 100 or student2_3 < 0 or student2_3 > 100:
    print("Error! Grades must be between 0 and 100")
    student2_1 = int(float(input("Please enter second student's midterm grade: ")))
    student2_2 = int(float(input("Please enter second student's project grade: ")))
    student2_3 = int(float(input("Please enter second student's final grade: ")))
print()
student3 = input("Please enter third student's name: ")
student3_1 = int(float(input("Please enter third student's midterm grade: ")))
student3_2 = int(float(input("Please enter third student's project grade: ")))
student3_3 = int(float(input("Please enter third student's final grade: ")))
while student3_1 < 0 or student3_1 > 100 or student3_2 < 0 or student3_2 > 100 or student3_3 < 0 or student3_3 > 100:
    print("Error! Grades must be between 0 and 100")
    student3_1 = int(float(input("Please enter third student's midterm grade: ")))
    student3_2 = int(float(input("Please enter third student's project grade: ")))
    student3_3 = int(float(input("Please enter third student's final grade: ")))
print()
student4 = input("Please enter fourth student's name: ")
student4_1 = int(float(input("Please enter fourth student's midterm grade: ")))
student4_2 = int(float(input("Please enter fourth student's project grade: ")))
student4_3 = int(float(input("Please enter fourth student's final grade: ")))
while student4_1 < 0 or student4_1 > 100 or student4_2 < 0 or student4_2 > 100 or student4_3 < 0 or student4_3 > 100:
    print("Error! Grades must be between 0 and 100")
    student4_1 = int(float(input("Please enter fourth student's midterm grade: ")))
    student4_2 = int(float(input("Please enter fourth student's project grade: ")))
    student4_3 = int(float(input("Please enter fourth student's final grade: ")))
print()
student5 = input("Please enter fifth student's name: ")
student5_1 = int(float(input("Please enter fifth student's midterm grade: ")))
student5_2 = int(float(input("Please enter fifth student's project grade: ")))
student5_3 = int(float(input("Please enter fifth student's final grade: ")))
while student5_1 < 0 or student5_1 > 100 or student5_2 < 0 or student5_2 > 100 or student5_3 < 0 or student5_3 > 100:
    print("Error! Grades must be between 0 and 100")
    student5_1 = int(float(input("Please enter fifth student's midterm grade: ")))
    student5_2 = int(float(input("Please enter fifth student's project grade: ")))
    student5_3 = int(float(input("Please enter fifth student's final grade: ")))

student1_passgrade = int(student1_1 * (0.3) + student1_2 * (0.3) + student1_3 * (0.4))
student2_passgrade = int(student2_1 * (0.3) + student2_2 * (0.3) + student2_3 * (0.4))
student3_passgrade = int(student3_1 * (0.3) + student3_2 * (0.3) + student3_3 * (0.4))
student4_passgrade = int(student4_1 * (0.3) + student4_2 * (0.3) + student4_3 * (0.4))
student5_passgrade = int(student5_1 * (0.3) + student5_2 * (0.3) + student5_3 * (0.4))

dictionary = {student1: ["Passgrade is {}".format(student1_passgrade)],
    student2: ["Passgrade is {}".format(student2_passgrade)], 
    student3: ["Passgrade is {}".format(student3_passgrade)],
    student4: ["Passgrade is {}".format(student4_passgrade)],
    student5: ["Passgrade is {}".format(student5_passgrade)]}

liste = []

for key, value in dictionary.items():
    temp = [key, value]
    liste.append(temp)
liste.sort(key=lambda x: x[1], reverse= True)

print (liste)
