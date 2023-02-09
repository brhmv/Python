import json

from datetime import date

yanacag={"Ai92" : 1,"Ai95" : 1.25,"Dizel": 0.80} 

fastfood={"Hotdog" : 2,"Cola" : 1,"Doner": 2.80}  



adm1={"Allahverdi" : "123456","Ceyhun": "654321"}


usr={"Xosrov":"123123","Eli":"321321"}
#json.dump(usr,open("users.txt","w"))
#json.dump(adm1,open("admins.txt","w"))
#json.dump(yanacag,open("yanacags.txt","w"))
#json.dump(fastfood,open("fastfoods.txt","w"))

def all():
    global yanacag
    global adm1
    global usr
    global fst
    adm1=json.load(open("admins.txt"))
    usr=json.load(open("users.txt"))
    fastfood=json.load(open("fastfoods.txt"))
    yanacag=json.load(open("yanacags.txt"))
    

    def adminyoxla():
        usera=input("Insert name: ")
        if usera in adm1:
       
            userp=input("Insert password:  ")
            if adm1[usera]==userp:
           
               print("Password is true")
               return True
            else:
                print("Password is false")
                adminyoxla()
        else:
            print("There isn't any admin like this")
            adminyoxla()

    def useryoxla():
        usera=input("Insert name: ")
        if usera in usr:
            userp=input("Insert password:  ")
            if usr[usera]==userp:
                print("Password is true")
                return True
            else:
                print("Password is false")
                useryoxla()
        else:
            print("There isn't any user like this")
            useryoxla()

    def benzinal():
        
        for i,j in yanacag.items():
            print(f" {i}--{j}")

        yy=input("Choose: ")
        if yy in yanacag:
            yl=int(input("How much:"))
            if yl>=1:
                print(f"********************\nprice {yl * yanacag[yy]} manats \nTarix--> {date.today()} \n********************")
            else:
                print("Minimum 1 litre")
                benzinal()
        else:
            print("Choose one of them:")
            benzinal()  

    def fastal():
        for i,j in fastfood.items():
            print(f" {i}--{j}")

        uf=input("Choose: ")
        if uf in fastfood:
            fq=int(input("How much:"))
            if fq>=1:
                print(f"********************\nprice {fq * fastfood[uf]} manats \nTarix--> {date.today()} \n********************")
            else:
                print("Minimum 1 piece ")
                fastal()
        else:
            print("Choose one of them:")
            fastal() 

    def yanbax():
        for i,j in yanacag.items():
                print(f" {i}--{j} \n")

    def fasbax():
        for i,j in fastfood.items():
                print(f" {i}--{j} \n")
        
    def delyan():
        yanbax()
        hs=input("Which one do you want to delete: ")
        if hs in yanacag :
            yanacag.pop(hs)
            json.dump(yanacag,open("yanacags.txt","w"))
            yanbax()
            all()
        else:
            print("Choose one of them.")
            delyan()
            all()

    def delfas():
        fasbax()
        hf=input("Which one do you want to delete: ")
        if hf in fastfood :
            fastfood.pop(hf)
            json.dump(fastfood,open("fastfoods.txt","w"))
            fasbax()
            all()
        else:
            print("Choose one of them.")
            fasbax()
            all()
        
    def addpet():
        yanbax()
        ha=input("Which one do you want to add: ")
        haq=float(input("Price of it: "))
        if ha not in yanacag :
            if haq>0:
                yanacag[ha]=haq
                json.dump(yanacag,open("yanacags.txt","w"))
                yanbax()
                
            else:
                print("Minimum 0.1 manat.")
                addpet()
                
        else:
            print("This petrol alraedy exist.")
            addpet()

    def addfas():
        fasbax()
        hfa=input("Which one do you want to add: ")
        fqn=float(input("Price of it: "))
        if hfa not in fastfood :
            if fqn>0:
                fastfood[hfa]=fqn
                json.dump(fastfood,open("fastfoods.txt","w"))
                fasbax()
                
            else:
                print("Minimum 0.1 manat.")
                addfas()
                
        else:
            print("This fastfood alraedy exist.")
            addfas()

    def adminis():
        as1=input("""1)Show petrols \n 2)Show fastfood \n 3)Delete petrol \n 4)Delete fastfood \n 5)Add petrol \n 6)Add fastfood \n 7)Exit """)
        if as1=="1":
            yanbax()
            adminis()
        elif as1=="2":
            fasbax()
            adminis()
        elif as1=="3":
            delyan()
            adminis()
        elif as1=="4":
            delfas()
            adminis()
        elif as1=="5":
            addpet()
            adminis()
        elif as1=="6":
            addfas()
            adminis()
        elif as1=="7":
            all()
        else:
            print("Choose one of them.")
   
    def useris():
        usersec=input("1)Oil \n 2)FastFood \n 3)Exit ")
        if usersec=="1":
            benzinal()
            ss=input("Do you want to buy fastfood? yes/no ")
            if ss=="yes":
                fastal()
                useris()
            elif ss=="no":
                benzinal()
            else:
                print("Write yes or no .")
        elif usersec=="2":
            fastal()
            useris()
        elif usersec=="3":
            all()
        else:
            print("Choose one of them.")
            
    g=input("""  1)User
      2)Admin      
                """)
    if g=="1":
        useryoxla()
        useris()

    elif g=="2":
        adminyoxla()
        adminis()

    else:
        print("Choose one of them.")
        all()
all() 

            





        

        

        


       


            
         
        
             