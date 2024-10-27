### Part Two -- your code goes here. 
import random
# Create a randome number from 1 to 100 inclusive
randnum = random.randint(1,100)
#print(randnum)
correct_guess = False

while correct_guess == False:
    # Check the input is an integer because funny errors haha
    guess = int(input("Guess the number (1-100): "))
    if guess == randnum:
        correct_guess = True
        print("Well done!")
    else:
        print("Nope")
