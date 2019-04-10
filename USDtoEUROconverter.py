Dollars = input("Please enter USD amount to be converted to Euros \n USD:")
Answer = float(Dollars) * .88
Bills50 = float(Answer) // 50
Bills20 = float(Answer) // 20
Bills10 = float(Answer) // 10
Bills5 = float(Answer) // 5

MoneyAfter50s = int(Answer) % 50
_20sAfter50s = int(MoneyAfter50s) / 20

MoneyAfter20s = int(_20sAfter50s) % 20
_10sAfter20s = int(MoneyAfter20s) / 10

MoneyAfter10s = int(_10sAfter20s) % 10
_5sAfter10s = int(MoneyAfter10s) / 5

MoneyAfter5s = int(MoneyAfter50s) % 5

print("Your Euro Ballance will be \n" + str(Answer) + "\nThere will be " + str(int(Bills5)) + " 5 Euro notes" + "\nThere will be " + str(int(Bills10)) + " 10 Euro notes" + "\nThere will be " + str(int(Bills20)) + " 20 Euro notes \n" + "There will be " + str(int(Bills50)) + " 50 Euro notes \n Most Efficient Euro Bills \n" + str(int(Bills50)) + " 50s " + str(int(_20sAfter50s)) + " 20s " + str(int(_10sAfter20s)) + " 10s and " + str(int(_5sAfter10s)) + " 5s, with " + str(int(MoneyAfter5s)) + " Euros after")
