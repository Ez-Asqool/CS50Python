# password attempts

def main():
    print("Welcome, Enter your valid login credentials")
    login()
    

def login():
    allowedAttempts = 4
    correctPassword = "123456"
    userName = input("User Name: ").strip()
    print("Hello", userName)
    while allowedAttempts > 0:
        password = input("Password: ")
        allowedAttempts -= 1 
        if password != correctPassword:
            if allowedAttempts == 0:
                print("Your account has been suspended due to repeated incorrect login attempts.!!")
            else:
                print(f"Invalid Login attempt. You have only {allowedAttempts} attempts left to log in.")
            
        else:
            print("Logged In Successfully")
            break
        

main()
