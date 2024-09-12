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
coffee_display = str(coffee_price)
if coffee_num == 1:
  print(coffee_num, 'Coffee at $' + coffee_display, 'each: $', format(coffee_total, '.2f'))
if coffee_num > 1:
  print(coffee_num, 'Coffees at $' + coffee_display, 'each: $', format(coffee_total, '.2f'))
if coffee_num == 0:
  print(coffee_num, 'Coffees at $' + coffee_display, 'each: $', format(coffee_total, '.2f'))
# combining coffee_num > 1 and coffee_num == 0 into if/or statement created bug
# where if coffee_num was 0, amount of coffees would not display on receipt
muffin_display = str(muffin_price)
if muffin_num == 1:
  print(muffin_num, 'Muffin at $' + muffin_display, 'each: $', format(muffin_total, '.2f'))
if muffin_num > 1 or muffin_num == 0:
  print(muffin_num, 'Muffins at $' + muffin_display, 'each: $', format(muffin_total, '.2f'))
  #if statements used to pluralize "coffee" and "muffin" in receipt when necessary
print('6% tax: $', format(tax_calc, '.2f'))
print('\n---------\n')
print('Total: $', format(final_cost, '.2f'))
#used format command to solve the lack of placeholder zero in displayed prices
print('***************************************')
