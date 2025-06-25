import random
digits = [random.randrange(1,5) for _ in range(4)]
pin =int("".join(map(str, digits)))
prompt = "yes"
answer = input("Would you like to generate your own pin?(yes/no): ")
if answer == prompt:
    print("Your generated pin is {}".format(pin))
else:
    print("Thanks!Come again later when you need to genrate your own pin")        
