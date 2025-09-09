expense_amount = float(input("Enter the expense amount: "))
manager_approval = input("Has the manager approved the expense? (yes/no): ")

# First, check if the expense amount is greater 0
if expense_amount > 0:
    # If the expense is greater than 0, now check if it is greater than 10000
    if expense_amount > 10000:
        # If the expense is greater than 10000, check if the manager has approved it
        if manager_approval.lower() == "yes":
            print("Expense approved and recorded:", expense_amount)
        # If the manager has not approved it, approval is still required
        else:
            print("Expense requires manager approval.")
    # If the expense is 10000 or less, it is automatically approved
    else:
        print("Expense approved and recorded:", expense_amount)
# If the expense is 0 or negative, it is invalid
else:
    print("Invalid expense amount. Please enter a positive value.")