menu = {
    "burger": 5.99,
    "fries": 2.49,
    "soda": 1.99,
    "salad": 3.49,
    "pizza": 8.99
}

cart = []
total = 0

# Print menu
for key, value in menu.items():
    print(f"{key.capitalize():10}:  ${value:5.2f}")
print("---------------")

# Take orders
while True:
    food = input("Select the food or (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]
    else:
        print("Item not on the menu.")

# Show order summary
print("\nYour Cart:")
for food in cart:
    print(f" {food.capitalize()}-${menu[food]:.2f}bur")

print(f"\nThe Total is: ${total:.2f}")