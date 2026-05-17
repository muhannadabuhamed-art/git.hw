print ("--eligibility tester--")

age = int(input("Enter your age: "))
bank_balance = float(input("Enter your bank balance: "))
if age >= 18 and bank_balance >= 100:
    print("You are eligible for the offer.")
else:    print("You are not eligible for the offer.") 

print(type(age))
print(type(bank_balance))