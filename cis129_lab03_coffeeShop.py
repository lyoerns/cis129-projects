#cis129_lab03_coffeeShop.py
"""Write a program that asks user for number of coffee and muffins they purchase
  and calculates the total price of their order plus tax."""
###
# objects: coffee_price; muffin_price; tax% (constants)
# user input: coffee_num and muffin_num
## coffee_total = coffee_num * coffee_price
## muffin_total = muffin_num * muffin_price

coffee_price = 5
muffin_price = 4
tax_per = .06
# above variables allow for easier modification of code 
# under real-world circumstances of fluctuating tax and item prices

# add if statement to pluralize coffee and muffins in receipt when necessary

print('***************************************\n')
print('My Coffee and Muffin Shop')
coffee_num = int(input('Number of coffees bought?\n'))
muffin_num = int(input('Number of muffins bought?\n'))
print('***************************************\n')


coffee_total = coffee_num * coffee_price
muffin_total = muffin_num * muffin_price
subtotal = coffee_total + muffin_total
tax_calc = subtotal * tax_per
final_calc = tax_calc + subtotal

# additional variable final_calc was created in order to use round command
# it didn't work when final_cost was rounded on its own
# python was adding too many decimal places to the printed final_cost

final_cost = round(final_calc, 2)

print('***************************************\n\nMy Coffee and Muffin Shop Receipt')
print(coffee_num, 'Coffee at $', coffee_price, 'each')
print(muffin_num, 'Muffins at $', muffin_price, 'each')
print('6% tax: $', tax_calc)
print('\n---------\n')
print('Total: $', final_cost)
print('***************************************')

