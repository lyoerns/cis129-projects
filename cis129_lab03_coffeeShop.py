#cis129_lab03_coffeeShop.py
"""Write a program that asks user for number of coffee and muffins they purchase
  and calculates the total price of their order plus tax."""
"""Update program to include two extra items on the menu and be able to calculate new total cost."""
###

coffee_price = 5
muffin_price = 4

tax_per = .06

#INSTRUCTIONS UPDATE: add two new menu items
mocha_price = 3
sand_price = 6

print('***************************************\n')
print('My Breakfast Shop')
coffee_num = int(input('Number of coffees bought?\n'))
muffin_num = int(input('Number of muffins bought?\n'))

mocha_num = int(input('Number of mochas bought?\n'))
sand_num = int(input('Number of sandwiches bought?\n'))
print('***************************************\n')


coffee_total = coffee_num * coffee_price
muffin_total = muffin_num * muffin_price
mocha_total = mocha_num * mocha_price
sand_total = sand_num * sand_price
subtotal = coffee_total + muffin_total + mocha_total + sand_total
tax_calc = subtotal * tax_per
final_calc = tax_calc + subtotal

# additional variable final_calc was created in order to use round command
# it didn't work when final_cost was rounded on its own
# round command added to fix python adding too many decimal places to displayed final cost

final_cost = round(final_calc, 2)

print('***************************************\n\nMy Breakfast Shop Receipt')
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

mocha_display = str(mocha_price)
if mocha_num == 1:
  print(mocha_num, 'Mocha at $' + mocha_display, 'each: $', format(mocha_total, '.2f'))
if mocha_num > 1 or mocha_num == 0:
  print(mocha_num, 'Mochas at $' + mocha_display, 'each: $', format(mocha_total, '.2f'))

sand_display = str(sand_price)
if sand_num == 1:
  print(sand_num, 'Sandwich at $' + sand_display, 'each: $', format(sand_total, '.2f'))
if sand_num > 1 or sand_num == 0:
  print(sand_num, 'Sandwiches at $' + sand_display, 'each: $', format(sand_total, '.2f'))
  
print('6% tax: $', format(tax_calc, '.2f'))
print('\n---------\n')
print('Total: $', format(final_cost, '.2f'))
#used format command to solve the lack of placeholder zero in displayed prices
print('Thank you for shopping at My Breakfast Shop!')
print('***************************************')
# Thank you for trying my program!
