foods = []
prices = []
total = 0

while True:
    food = input("Enter the Food (q to quit):")
    if food.lower() == "q":
     break
    else:
       price = float(input("Enter the price : $"))
       foods.append(food)
       prices.append(price)

print("----Your Shopping Cart---")
for food in foods :
   print(f"{food} - {price}")

for price in prices :
   total = total + price

print(f"The total price is: {total}")   