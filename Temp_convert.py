unit = input("Enter the temperature in Celsius or Fahrenheit  (C or F) :")
temp = float(input("Enter the temperature to be convert : "))

if unit == "C" or unit == "c"  :
    temp = round((9 * temp) / 5 + 32 ,2)
    print(f"The Temperature in Fahrenheit  is {temp}°C")
elif unit == "F" or unit == "f" :
    temp = round((temp - 32) * 5 / 9 , 2)
    print(f"The Temperature in Celsius is {temp}°F")
else :
    print(f"The unit you entered {unit} is  wrong")
    