# x = int(input("Enter any number: "))

# match x:

#     case x if x < 10:
#         print("It is a one-digit number")
#     case x if 10 <= x < 100:
#         print("It is a two-digit number")
#     case x if 100 <= x <= 999:
#         print("It is a three-digit number")
#     case _:
#         print("It is a larger than three-digit number")

x = int(input("Enter any two number for calculation: \nEnter the first number is :- \n"))
y = int(input("Enter the second number:- \n"))
c = int(input("Enter your choice :-\n1.Addition\n2.Substration\n3.Multiplication\n4.division\n"))

match c:

    case c if c == 1:
        print("The sum of x and y is \n",x+y)

    case d if d == 2:
        print("The sub of x and y is \n",x-y)
    
    case d if d == 3:
        print("The mul of x and y is \n",x*y)
    
    case d if d == 4:
        print("The div of x and y is \n",x/y)

    case _:
        print("You have entered the wrong choice,\n SORRY, Please try again")


