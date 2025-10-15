
foods = []
prices =[]
total = 0

while True:
    food = input("Enter food you are buying or q for quit")
    if food.lower()  == 'q':
        break  
    else:
       price = float(input(f"Enter price of the {food}:R"))
       foods.append(food)
       prices.append(price)

print("*************Cart List******************")

for food in foods:
    print(food)

for price in prices:
    total += price
    print("\n")
    print(f"Your total is: R{total}")



