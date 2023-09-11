import random
from art import logo
from replit import clear

def blackjack():
  print(logo)
  should_continue=True
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def deal():
    n=random.randint(0,12)
    return cards[n]
  s=0

  def add(list):
    s=sum(list)
    if 11 in list and 10 in list and len(list)==2:
      s=0
    elif s>21 and 11 in list:
      user.remove(11)
      user.append(1)
      s=sum(list)
    return s
    
  user=[]
  comp=[]
  user.append(deal())
  user.append(deal())
  comp.append(deal())
  comp.append(deal())
  user_score=0
  comp_score=0
  while should_continue:
    user_score=add(user)
    comp_score=add(comp)
    print(f"Your cards are {user}. Your score is {user_score}.\nThe computer has [{comp[0]}, X].")
    
    if(user_score==0 or comp_score==0 or user_score>21):
      should_continue=False
    else:
      ch=input("Do you want to pick another card? Type 'y' or 'n': ")
      if ch=="y":
        user.append(deal())
      else:
        should_continue=False
  
  while comp_score<17 and comp_score!=0:
    comp.append(deal())
    comp_score=add(comp)
  
  def compare(user_score, comp_score):
    print(f"Your final hand: {user}.\nThe computer's final hand: {comp}.")
    if user_score==comp_score:
      print("DRAW")
    elif user_score==0 or user_score==21 or comp_score>21:
      print("USER WINS")
    elif comp_score==0 or comp_score==21 or user_score>21:
      print("COMPUTER WINS")
    else:
      if user_score>comp_score:
        print("USER WINS")
      else:
        print("COMPUTER WINS")
    c=input("Do you want to play again? Type 'y' or 'n': ")
    if c=="y":
      clear()
      blackjack()
  compare(user_score, comp_score)
  
blackjack()
      
