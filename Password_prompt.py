passwd = "Kashbaby023"
username ="Kashbaby"
attempts = 0
user_name =str(input("Please input username: "))
userPass =str(input("Please enter your Password: "))

while attempts < 3:
    if user_name == username and userPass == passwd:
        print("Access granted")
        break
    else:
        print("Acess Denied")
        attempts+= 1  


       
