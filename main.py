# perfect guess game
import random

n = random.randint(1,45) # 1 and 20 are included
count = 0

while True:  # keeps loop runnig forever
    m = int(input("Guess the number: "))
    count +=1
    if (n > m):
        print("Guess for higher number please!")
    elif(n < m):
       print("Guess for lower number please!")       
    else:
       print(f"You guessed it righttt number is {n}")
       print(f"total guess: {count}")