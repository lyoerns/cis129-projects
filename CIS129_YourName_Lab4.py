# Module 4 Lab_4
#Lee Yoerns
# 22 September 2024
# Calculates store bonus and employee bonus based on user input\
    # of monthly sales and sales increase
# Prints a message depending on the employee and store bonuses

storeAmount = 0
empAmount = 0
salesIncrease = 0
monthlySales = 0


#code to get monthly sales:
monthlySales = float(input("Enter Amount of Monthly Sales: "))

#code to calculate store bonus:
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

#code to get inc. in sales:
salesIncrease = float(input("Enter Percentage of Sales Increase: "))
salesIncrease = salesIncrease / 100

#code to calculate employee bonus:
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#code to print results:
print("The store bonus amount is $", storeAmount) 
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print("Congrats! You have reached the highest bonus amounts possible!")