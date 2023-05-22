v = ["c1", "c2", "c3", "c4", "c5"]
n = len(v)
for i in range(n+1):
    w = input("please enter your vehicle type : ")
    if w == "bike":
        c1 = int(input("please pay toll Rs. 100 : "))
        if c1 == 100:
            v.pop(0)
            print("......Thank You......Happy Journey......")
            print("_Remaining vehicles_\n")
            print(v)
        else:
            print(" we can't open the door until you pay Rs.100, please pay again")
    elif w == "car":
        c1 = int(input("please pay toll Rs. 200 : "))
        if c1 == 200:
            v.pop(0)
            print("......Thank You......Happy Journey......")
            print("Remaining vehicles")
            print(v)
        else:
            print(" we can't open the door until you pay Rs.200, please pay again ")
    elif w == "truck":
        c1 = int(input("please pay toll Rs. 300 : "))
        if c1 == 300:
            v.pop(0)
            print("......Thank You......Happy Journey......")
            print("Remaining vehicles")
            print(v)
        else:
            print(" we can't open the door until you pay Rs.300, please pay again ")
    else:
        print("This type of vehicle is not allowed")
        