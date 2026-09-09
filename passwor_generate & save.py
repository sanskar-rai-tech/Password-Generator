import random
import string
password={}
try:
    with open("password.txt","r") as file:
        for line in file:
            website,password=line.strip().split(":")
            password[website]=pswd 
except:
    pass 

def generate_password():
    char=string.ascii_letters + srting.digits + "!@#$%^&*()_+=-"
    password="".join(random.choice(char) for _ in range(9))
    return password
while True:
    print("PASSWORD MANAGER")
    print("1.SAVE PASSWORD")
    print("2.VIEW PASSWORD")
    print("3.GENERATE PASSWORD")
    print("4.EXIT")
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice=="1":
        web=input("ENTER YOUR WEBSITE :")
        pswd=input("ENTER YOUR PASS :")

        password[web]=pswd
        with open("password.txt","a") as file:
            file.write(f"{web} : {pswd}\n")
        print("password save successfully")
    elif choice=="2":
        if not password:
            print("no passs")
        else:
            for web,pswd in passwords.items():
                print(web,":",pswd)
    elif choice=="3":
        print("generate pass :",generate_password())
    elif choice=="4":
        print("thankyou for visit")
        break
    else:
        ("please enter valid number ")

