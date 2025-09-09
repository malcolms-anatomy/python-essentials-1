# When we use if alone, we only care whether the condition is true.
# If it is false, we do nothing.

expense = float(input("Enter an expense amount: "))

# Only check if the expense is valid
if expense >= 0:
    print("Expense recorded:", expense)
    print("Thank you for your input.")
    print("Have a nice day!")

else:
    print("Invalid expense amount. Please enter a non-negative value.")