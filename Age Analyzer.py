age = int(input("How old are you in years?"))
lifeleft = 115 - int(age)
afterlife = int(age) - 115
if age > 18:
    print("You are eligible to vote!")
else:
    print("You are not old enough to vote yet.")

if age > 65:
    print("You are of age to retire!")
else:
    print("You are not able to retire yet")

if age > 115:
    print("But, you are likely to be dead. RIP in pieces my friend, probs been dead for " + str(afterlife) + " years.")
else:
    print("Assuming maximum life span you have " + str(lifeleft) + " years left. Enjoy them")

