operator = input("Enter any Operator (+,-,*,/) :")
first_value = float(input("Enter 1st value :"))
second_value = float(input("Enter 2nd value :"))

if operator == "+" :
    addition = first_value + second_value
    print(addition)
elif operator == "-" :
    subtraction = first_value - second_value
    print(subtraction)
elif operator == "*" :
    multiplication = first_value * second_value
    print(multiplication)
elif operator == "/" :
    division = round(first_value / second_value , 2)
    print(division)
else :
    print("You entered wrong operator , kindly enter from any of these (+,-,*,/)")