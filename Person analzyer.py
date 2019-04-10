currentyear = 2019
name = input("Enter your name:")
age = int(input("Age:"))
yearsto100 = 100 - int(age)
yearwillreach100 = int(yearsto100) + int(currentyear)
print(str(name) + ", you are " + str(age) + " years old")
if age < 100:
    print("You have " + str(yearsto100) + " years till you reach 100 years old. You will turn 100 in about the year " + str(yearwillreach100))