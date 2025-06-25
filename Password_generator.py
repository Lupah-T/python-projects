import random
import string
import secrets
userPassd =("".join(random.choice(string.ascii_letters + string.digits + string.hexdigits + string.punctuation ) for _ in range(12)))
prompt = "Yes"
userChoice = input("Would you like us to generate a password for you?(Yes/No): ")
if userChoice == prompt:
    print("Your Generated Password is {}".format(userPassd))
else:
    print("Please come again later when you need to generated a password")    
