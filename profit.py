days = 2

for day in range(days):
    day = input("Enter the day : ")
    sales = int(input("Enter the number of sales : "))
    for sale in range(sales):
        gas_type = int(input("Enter the gas type : "))
        S_price = int(input("Enter the selling price : "))

if(gas_type == 1):
    price = 200
elif(gas_type == 2):
    price = 300
elif(gas_type == 3):
    price = 400
elif(gas_type == 4):
    price = 500

T_sales = 0
for i in range(sales):
    T_sales = T_sales + sales

T_profit = 0
for i in range(T_sales):
    profit = S_price - price
    T_profit = T_profit + profit

print("The profit of that week is", T_profit)
