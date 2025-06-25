import random
number = random.randint(1,20) #takes a random integer between 1 and 20
print("Im thinking of a number between 1 and 20....")
while True: #while the conditions are true,then the code continues
    guess = int(input("Enter you guessed number: ")) #prompts user to enter his/her guesed number
    if guess <number:
        print('Your guess is too low')
    elif guess > number:
        print("Your guess is too high")
    else:
        print("You guseed right")   
        break 
    
                  
  
        
