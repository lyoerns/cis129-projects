# Write program that asks user for number of coffee and muffins they purchase
# Price of coffee is $5 and price of muffin is $4. Calculate 6% tax on subtotal. 
###

# objects: coffee_price and muffin_price (constant)
# user input: coffee_num and muffin_num
## coffee_total = coffee_num * coffee_price
## muffin_total = muffin_num * muffin_price
# sum of muffin_total + coffee_total (sum = subtotal)

#must multiply sum by tax (1.06) = final_cost

coffee_num = int(input('Number of coffees bought?\n'))
muffin_num = int(input('Number of muffins bought?\n'))
coffee_price = 5
muffin_price = 4
coffee_total = coffee_num * coffee_price
muffin_total = muffin_num * muffin_price
subtotal = coffee_total + muffin_total
final_calc = subtotal * 1.06
final_cost = round(final_calc, 2)
print('Total: $', final_cost)
