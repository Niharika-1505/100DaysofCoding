from replit import clear
from art import logo


def highest_bidder(bidders_dict):
    max_value = max(bidders_dict.values())
    for key, value in bidders_dict.items():
        if max_value == value:
            print(f"The winner is {key} and they bid £{value}.")


print(logo)

bidders = {}
bidding_end = False
while not bidding_end:
    bidder_name = str(input("Please enter the bidder name: "))
    bid_amount = float(input("Enter the bid amount: "))
    bidders[bidder_name] = bid_amount
    restart = input("Type 'yes' if there are more bidders.Otherwise type 'no'.\n")
    if restart.lower() == "no":
        bidding_end = True
        print("Auction ended")
    else:
        clear()

highest_bidder(bidders)
