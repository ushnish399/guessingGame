import random
print("Number guessing Game")
number=random.randint(0,9)
chances=0
print("guess the number between 0 and 9")
while(chances < 5):
    guess=int(input("enter your number"))
    if(guess==number):
        print("CONGRATULATIONS!!!")
        break
    elif(guess>number):
        print("TRY SOMETHING LOWER")
    else :
        print("TRY SOMETHING HIGHER")
    chances= chances + 1
if(chances>=5):
    print("PLEASE TRY AGAIN")


