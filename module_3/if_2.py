invoice = float(input("Enter an invoice amount: "))
vat_registered = input("Is the customer VAT registered? (yes/no): ")

# Only check if the customer is VAT registered
if vat_registered.upper() == "YES":
    vat = invoice * 0.075
    print("VAT applied:", vat)
    print("Total with VAT:", invoice + vat)

else:
    print("No VAT applied.")
    print("Total amount:", invoice)
