#1.Understand the problem
#2.think
#3.algorithm
#4.main logic and start working
#5.modify

#algorithm
#1.develop random face no
#2.check no
#3.print faces
#4looping
import random
print("This is a dice stimulator ")
x="y"
while x == "y":
    num=random.randint(1,6)
    if num==1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    elif num==2:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")    
    elif num==3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------") 
    elif num==4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    elif num==5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    elif num==6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------") 
    x=input("Press y to roll again : ")