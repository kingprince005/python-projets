
#to escap the charector we use \ 
#also we use \n for next line 
# print("hey dude \"how are you!\" \nwhat's going on?")

# # we use this sep= to seprate the all value and string and variable between the charector or number
# #we also use end= sepratot to print enything in the last of the line ex-

# print ("hey",2,3.0,sep= "  ", end=" mumed\n")
# print("printing after the mumed statement")

#calculator program using python, using function, using arguments, using while loop, using break statement, using arithmetic oprations, 😂😎

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def div(x,y):
    return x/y
 
print("there are some arithmetic function to perform in this calculator 😊")
print("1: addition 😊")
print("2: substraction😉")
print("3:multiplication😄")
print("4:dividation😜")

while True:

    choise=(input("enter your choise 1/2/3/4 🤷‍♂️🙌-"))

    if choise in ('1','2','3','4'):
        try:
            num1=float(input("enter first number 😉-"))
            num2=float(input("enter second number 😜-"))

        except ValueError:
            print("invalid input😒. plese enter the number 👍-")
            continue

    if choise == '1':
        print(num1, "😘", num2, "=😍", add(num1,num2))
    
    elif choise == '2':
        print(num1, "😊", num2, "=😍", subtract(num1,num2))

    elif choise == '3':
        print(num1, "🙃", num2, "=😍", multiply(num1,num2))

    elif choise == '4':
        print(num1, '😚', num2, '=😍', div(num1,num2))

    next_calculation = input("let's do next calculation (yes/no)😉👍 :")
    if next_calculation == "no":
        break
    elif next_calculation == "yes":
        continue
    else:
       print("ivalide input😒")

