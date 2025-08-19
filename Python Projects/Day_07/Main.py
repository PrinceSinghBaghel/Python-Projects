def finding(bidding_counter):
    winner=""
    highest_bid = 0
    for bidder in bidding_counter:
        bid_amount = int(bidding_counter[bidder])
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner= bidder

    print(f"The winner is {winner} with a bid of Rs.{highest_bid}.")

print("Welcome to the secret auction programme")

bidding_counter={}



flag=True
while flag:
    key=input("What is your name?: \n")
    value=input("What's your bid?: \n")

    bidding_counter[key]=value


    continue_counter=input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if continue_counter=="no":
        flag=False
        finding(bidding_counter)
    elif continue_counter=="yes":
        print("\n"*20)


