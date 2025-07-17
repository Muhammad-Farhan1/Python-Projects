#Interest rate calculator:
principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter the principle value:"))
    if principle <= 0:
        print("Principle can't be negative or less than zero")

while rate <= 0:
    rate = float(input("Enter the value of interest rate:"))
    if rate <= 0:
        print("interest rate can't be negative or less than zero")

while time <= 0 :
    time = int(input("Enter the time:"))
    if time <= 0:
        print("Time can't be negative or less than zero")

amount = round(principle * pow((1 + rate / 100) , time) , 2)       

print(f"The value of interest after {time} is : {amount} pkr")