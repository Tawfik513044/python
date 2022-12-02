# def multiply(x,y):
#     return x * y

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))

# print(number1, "*", number2, "=", multiply(number1, number2))


 #  Ik moet nog een paar dingen fixen.


num1 = input("voer je eerste cijfer in:")
num2 = input("voer je tweede cijfer in:") 

x1 = num1.isnumeric()
x2 = num2.isnumeric()


if x1 == True and x2 == True:
    num1 =int(num1)
    num2 = int(num2)
    print (num1 * num2)
else:
    print(" je moet cijfer invullen")




# x = str(3)    # x will be "3"
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0