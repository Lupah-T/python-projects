import random
print("WELCOME TO THE GAMELROCK,PAPER,SCISSORS.")
def game():
   playerChoice = str(input("Please Enter your Chioce(Rock,paper,Scissors): "))
   compChoice = random.choice(["Rock","Paper","Scissors"])
   if playerChoice == compChoice:
      print("Correct!You Got it Right :()")
   elif playerChoice != compChoice:
       print("Oppsy!Try again :(")
       print("Thanks Champ :)")    
output = game()
print(output)