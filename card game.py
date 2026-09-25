import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_or_not = input("Do you want to play or not? Type 'y' or 'n'\n")
if play_or_not == 'y':
   card_1 = random.choice(cards)
   card_2 = random.choice(cards)
   computer_1 = random.choice(cards)
   computer_2 = random.choice(cards)
   print(f"Your cards: [{card_1},{card_2}], current score: {card_1+card_2}")
   print(f"Computer's first card: {computer_1}")
   another_card = input("Type 'y' to get another card, type 'n' to pass:\n")
   if another_card == 'y':
       cards = [card_1, card_2]
       computer_cards = [computer_1, computer_2]
       while another_card != 'n':
           cards.append(random.choice(cards))
           computer_cards.append(random.choice(cards))
           print(f"Your card is now {cards}")
           print(f"Computer's third card was {computer_cards[-1]}")
           another_card = input("Type 'y' or 'n': ")
       def my_total_points():
               total_my_points = 0
               for card in cards:
                   total_my_points += int(card)
               return total_my_points
       def computers_total_points():
               total_computer_points = 0
               for card in computer_cards:
                   def computers_total_points():
                       total = 0
                       for card in computer_cards:
                           total += card
                       return total
               return total_computer_points
       print("your total points: " + str(my_total_points()))
       print("computer total points: " + str(computers_total_points()))
       if 21 > my_total_points() > computers_total_points():
           print("You win!")
       elif 21 > computers_total_points() > my_total_points():
           print("Computer wins!")
       elif computers_total_points() == my_total_points():
           print("Its a tie!")
       elif my_total_points() > 21:
           print("Brust")
   else:
       my_point = card_1 + card_2
       computer_point = computer_1 + computer_2
       print(f"computer second card was {computer_2} and its points was {computer_point}")
       if  21 > my_point > computer_point:
           print("You win!")
       elif 21 > computer_point > my_point:
           print("Computer wins!")
       elif computer_point == my_point:
           print("Its a tie!")
       elif my_point > 21:
           print("Brust")

