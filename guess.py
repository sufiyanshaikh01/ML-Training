import random 

secret = random.randint(1, 1000)
attempt = 0
max_attempt = 5

while attempt < max_attempt:
    attempt += 1
    user = int(input("Guess the number is: "))
    
    if user == secret:
        print(f"You win at {attempt} attempt")
        break
    elif user < secret:
        print("To Low")
    else :
        print("To High")
else:
       print ("Sorry your are lose the Game.😂")
       print(f"Your number is {secret}")