n = int(input("Please enter an single digit integer: "))

while (n > 9 or n < 0):
    n = int(input("Your number is not a single digit. Please enter an single digit integer: "))
for num in range(n+1):
    if num % 2 == 0:
        print(num)
