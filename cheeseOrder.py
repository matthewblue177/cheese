# Price per pound $10
# Min amount - 5 pounds
# Max ammound - 100 pounds
import time

def cheeseOrder(cheese):
    int(cheese)
    total = int(cheese) * 10
    return str(total)

valid = 0
while valid == 0:
    cheeseAmount = input ('How much cheese would you like in lbs? : ')
    if int(cheeseAmount) < 5:
        print ("That is not enough cheese to make an order!")
        time.sleep (2)
    elif int(cheeseAmount) > 100:
        print ('That is too much cheese to ship!')
        time.sleep(2)
    elif cheeseAmount.isalpha():
        print ('The ammount must be a number!')
    else:
        print ('Ok... let me just price it out for you!')
        time.sleep (2)
        print ('Adding up cheese!')
        time.sleep (2)
        valid = 1
print ('The price of your cheese will be $' + cheeseOrder(cheeseAmount))
time.sleep (2)
valid = 0
while valid == 0:
    print ('Would you like to place your order?')
    confirmation = input()
    confirmation = confirmation.lower()
    if confirmation == "yes":
        print ('Order placed!')
        valid = 1
    elif confirmation == 'no':
        print ('Ok, order canceled!')
        valid = 1
    else:
        print ("Sorry! I didn't get that, please try again!")
        time.sleep (2)
