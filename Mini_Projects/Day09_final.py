#Auction bitting

'''
1. ask for name and save it
2. ask for amount and save it
3. ask is there anyone else betting
4. if yes, then loop through above, if no show the one with highest bit'''


def bitter_list(name_of_person,amount_bitted):
    auction_bitters[name_of_person]=amount_bitted

print("Welcome to Auction")

auction_bitters={}
to_bit=True 

while to_bit:
  name=input("Enter Your Name: ")
  amount=int(input("Enter the amount: $"))
  another_bit=input("Is there anyone else to bit, type 'yes' or 'no' \n").lower()
  if another_bit=="yes":
    bitter_list(name,amount)
    continue
  else:
    bitter_list(name,amount)
    max_bitter=""
    max_bit=0
    for bits in auction_bitters:
       if max_bit<auction_bitters[bits]:
          max_bit=auction_bitters[bits]
          max_bitter=bits
    print(f"The Auction won by {max_bitter}, bitten amount {max_bit}$")
    to_bit=False


#or
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    continue