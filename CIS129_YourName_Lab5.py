#Lee Yoerns
#30 September 2024
"""Allow data regarding daily number of bottles to be input and calculate today number of bottles
for seven days, and the payout of the total times .10 cents"""
#Lab 5 The Bottle Return Program
# declare unchanging variables:
NBR_OF_DAYS = 7
PAYOUT_PER_BOTTLE = .10 
keep_going = 'y'
while keep_going == 'y': # initialize program; allow for multiple runs
    counter = 1     # declare variables that must be reset to 0 every run
    total_payout = 0
    total_bottles = 0
    today_bottles = 0
    while counter <= NBR_OF_DAYS: # makes sure program knows when to stop requesting data for current run
        print('Enter number of bottles returned for day #', counter)
        today_bottles = int(input('Number of Bottles: '))
        # note: had to make lines 15 and 16 separate; kept getting typeError otherwise
        total_bottles += today_bottles
        counter += 1   
    total_payout = total_bottles *  PAYOUT_PER_BOTTLE
    print("Total Bottles:", total_bottles)
    print("Total Payout: $", format(total_payout, '.2f'))
    print("Do you want to enter another week's worth of data?")
    keep_going = input("(Enter y or n)")
