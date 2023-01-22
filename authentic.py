# Project Name : Login & Signup | using Database 
# Uses of Def Function and file handling txt file format append function , List , dictionary
# Advanced Skills Required : Html and Css , GUI

def welcome():
    	print("Welcome to your Dashboard")
welcome()

def register():
    db = open("database.txt","r")
    Username = input("Create UserName  : ")
    Password = input("Create PassWord  : ")
    Password1 = input("Confrim PassWord : ")

    d = []
    f = []
    for i in db:
        a,b = i.split(" , ")       # This is will help to giving the space bettween in database username and password
        b = b.strip()  
        d.append(a)                # d is storing the username not gonna repeat next time when you using the existed username from database
        f.append(b)  
    data = dict(zip(d,f))  
   # print(data)                               # With this all code you will get output of your all stored database into Dictionary format 

    if Password != Password1:
        print("PassWords Don't Match , Restart ") 
    else:
        if len(Password)<=6:
            print("PassWord Too Short , Restart ")
            register()
        elif Username in d:
           print("username exists")
           register()
        else:
            db = open ("database.txt","a")
            db.write(Username+" , "+Password+"\n")
            print("Success ! ")



def access():

    db = open ("database.txt","r")
    Username = input("Enter Your  UserName  : ")
    Password = input("Enter Your  PassWord  : ")

    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(" , ")      
            b = b.strip()  
            d.append(a)                
            f.append(b) 
        data = dict(zip(d,f))

        try:                                # The try block lets you test a block of code for errors.
            if data[Username]:
                try:
                    if Password ==data[Username]:
                        print("Hi,", Username)
                        print("Login Success")
                    else:
                        print("PassWord or  UserName is incorrect")
                except:
                    print("Incorrect Password or UserName")
            else:
                print("UserName  or PassWord Doesn't existed ")
        except:
            print("Username and PassWord Doesn't existed ")
    else:
        print("Please Enter a Value ")

def home(option=None):                           # This Def function will help you for reach out the Login and Signup Functions 
    option = input("Login|SignUp: ")
    if option == "Login" or "login" or "LOGIN":
        access()
    elif option == "SignUp" or"signup" or "SIGNUP":
         register()
    else:
        print("Oops, Something went  wrong . please try again later 404")

home()