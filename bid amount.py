import os
from time import sleep
logo = '''
 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
print(logo)
should_continue = True
# create an empty dictionary and store the name and amount to it as key value pair where name is key.
bids = {}
# create a function to compare the bid amounts- step4
def maximum_bid_amount(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amt = bid_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with a bid amount of {highest_bid}")


# make program run in loop by using while loop - step5
while should_continue:
    # create a variable to store name - step1
    name = input("Please Enter Your Name ? : ")
    # create a variable to store the bid amount - step2
    bid_amount = int(input("Enter your bid amount : $"))
    bids[name] = bid_amount
    cont = input("Are there other bidders ? Type YES of NO\n").lower()
    if cont == "yes":

        os.system('cls')
        sleep(1)

    elif cont == "no":
        should_continue = False
        maximum_bid_amount(bids)
    else:
        print("Wrong Input. Try Again.")
