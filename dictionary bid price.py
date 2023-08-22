import os
def screen_clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

bidders = {}

logo = '''

     3/1    2/1     1/1     2/3     1/2
|    |      /      /      .'      .'
|    |     |      /      /      .'
|    /     /     /     .'     .'          1/3
|   |     |     /     /     .'         .-'
|   |     /    /    .'    .'        .-'
|   /    |    /    /    .'       .-'       1/4
|  |     /   /   .'   .'      .-'      _.-'
|  |    |   /   /   .'     .-'     _.-'      1/5
|  /    /  /  .'  .'    .-'    _.-'     _.--'
| |    |  /  /  .'   .-'   _.-'    _.--'      1/6
| |    / / .' .'  .-'  _.-'   _.--'     __.--'     1/7
| |   | / / .' .-' _.-'  _.--'    __.--'    __..--'
               _.-' _.--'   __.--'   __..--'    1/8
               _.--'  __.--'  __..--'   __..--''
                __.--' __..--'  __..--''
                __..--' __..--''
                __..--''
'''

def find_highest_bidder(bidding_records):
    """finds out the highest bidder in the dictionary"""
    winner = ""
    highest_bid = 0
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the auction is {winner} with a bid amount of ${bid_amount}")





print(logo +"\nWelcome to the auction program")

should_continue = True
while should_continue:
    user_name = input("Please enter your name here : ").title()
    bid_amount = int(input("Please enter your bid amount here : "))
    bidders[user_name] = bid_amount
    any_other_bidders = input("Are there any other bidders ? : Type Y or N : ").lower()
    if any_other_bidders == "y":
        screen_clear()
    if any_other_bidders == "n":
        should_continue = False
        find_highest_bidder(bidders)

