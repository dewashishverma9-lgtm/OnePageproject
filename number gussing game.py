import random


easy_or_hard = input("Chose a fificulty. Type 'easy' or 'hard'")
easy_or_hard = easy_or_hard.lower()






numbers = []
for number in range(1, 101):
   numbers.append(number)


s_num = int(random.choice(numbers))


print(s_num)


def hard(num):
   global selected_number
   attempt = 5
   print("You have 5 attempt to guess the number")
   while attempt > 0:
       guess = int(input("Guess the number: "))
       attempt -= 1
       if guess == num:
           print("You guessed the number")
           return
       elif guess > num:
           print("Too high")
       elif guess < num:
           print("Too low")


def easy(num):
   attempt = 10
   print("You have 10 attempt to guess the number")
   while attempt > 0:
       guess = int(input("Guess the number: "))
       attempt -= 1
       if guess == num:
           print("You guessed the number")
           return
       elif guess > num:
           print("Too high")
       elif guess < num:
           print("Too low")




if easy_or_hard == 'easy':
   easy(s_num)
elif easy_or_hard == 'hard':
   hard(s_num)

