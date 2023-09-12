import art
import game_data
import random
from replit import clear

def correct_ans(entry1,entry2):
  entry1=entry2
  clear()
  return entry1

def wrong_ans(count):
  clear()
  print(f"Sorry, that's wrong. Final score: {count}")
  
count=0
is_going=True

entry1=random.choice(game_data.data)
name1=entry1["name"]
description1=entry1["description"]
country1=entry1["country"]
follower_count1=entry1["follower_count"]


while is_going==True:
  print(art.logo)
  print(f"Compare A: {name1}, a {description1}, from {country1}")
  print(art.vs)

  entry2=random.choice(game_data.data)
  name2=entry2["name"]
  description2=entry2["description"]
  country2=entry2["country"]
  follower_count2=entry2["follower_count"]
  print(f"Against B: {name2}, a {description2}, from {country2}")
  answer=input("Who has more followers? Type 'A' or 'B':").capitalize()
  
  if answer=="A":
    if follower_count1 > follower_count2:
      entry1 =correct_ans(entry1,entry2)
      count+=1
      print(count)
    else:
      wrong_ans(count)
      is_going=False
      
  elif answer =="B":
    if follower_count2 > follower_count1:
      entry1 =correct_ans(entry1,entry2)
      count+=1
    else:
      wrong_ans(count)
      is_going=False
      
      