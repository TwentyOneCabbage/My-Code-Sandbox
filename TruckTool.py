Truck_H = int(input("MOVERS CALCULATOR \n Input the Dimensions of your truck in inches. \n Enter its height:"))
Truck_W = int(input("Enter its width"))
Truck_D = int(input("Enter its depth"))
Truck_A = int(Truck_H * Truck_W * Truck_D)

Object_H = int(input("now, enter your Objects height:"))
Object_W = int(input("Enter its width:"))
Object_D = int(input("Finally enter its Depth"))
Object_A = int(Object_H * Object_W * Object_D)

Area_NoObj = int(Truck_A - Object_A)
Phrase1 = " cubic inches..."
print("Trucks volume:" + str(Truck_A) + Phrase1 + "Object volume:" + str(Object_A) + Phrase1 + "Volume left in truck:" + str(Area_NoObj) + Phrase1)