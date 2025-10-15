import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

invest = input("Enter either 'Investment' or 'Bond' from the menu above to proceed")

if invest.lower() == 'investment':
    deposit = float(input("Enter amount you want to deposit"))
    rate = float(input("Enter interest rate excluding '%' sign"))
    year = float(input("Enter how many years you want to invest"))
    interest= input("Enter your investment type is it: SIMPLE or COMPOUND")

    if interest.lower() == 'simple':
        payOutS = deposit *(1 + rate * year)

        print(f"Total payout :R{payOutS}")

    elif interest.lower() == 'compound':
        payOutC = deposit * math.pow((1 + rate),year)
        print(f"Total payout :R{payOutC}")

elif invest.lower() == 'bond':
    house = float(input("Enter present value of the house"))
    intRate = float(input("Enter interest rate"))
    month =int(input("Enter number of month planned to repay/bond"))

    bondPay =(month * intRate)/(1 - (1 + intRate)**(- month))
    print(f"Your bond invest is :R{bondPay}")
