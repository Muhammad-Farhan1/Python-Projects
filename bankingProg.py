def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount you want to deposit: "))
    if amount <= 0:
        print("Please enter an amount greater than zero")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount you want to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount <= 0:
        print("Please enter an amount greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 0          
    isRunning = True 

    while isRunning:
        print("*********************")
        print("Enter (1-4) for :")
        print("1: Current Balance")
        print("2: Deposit Money")
        print("3: Withdraw Money")
        print("4: End")
        print("*********************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            isRunning = False
        else:
            print("You entered an invalid number.")

    print("Goodbye! Have a nice day <3")

if __name__ == '__main__':
    main()
