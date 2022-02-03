import random

print("welcome login signup ")
print("login 1")
print("signup 2")
user=input("prees and button...")
if user==2:
    name=input("enter name...")
    password=input("password and strong...")
    upper,lower,s,digit=0,0,0,0
    if len(password)>=7:
        for i in password:
            if (i.isupper()):
                upper=1            
            if (i.islower()):
                lower=1
            if (i.isdigit()):
                digit=1
            if(i=="@"or i=="#"or i=="$" or i=="%" or i=="^" or i=="&") :
                s=1
        total=upper+lower+s+digit
        if total!=4:
            print("please button atlest one capital letter ,small letter ,digit and s character")
        else:
            password2=input("comfrom password")
            if password!=password2:
                print("please com password ")
            elif password==password2:
                s=open("shivani.json","r")
                j=s.read()
            if name in s:
                print("",name,"you are alread exist")
                print(s)
            else:
                hobby=input("Enter your Hobbies:")
                Designation=input("Enter your Designation:")
                Birth=input("enter your Date of Birth:")
                Gender=input("Enter your Gender:")
                d={}
                l=[]
                d['Username']=name
                d["Password"]=password
                d['Hobbies']=hobby
                d["Gender"]=Gender
                d["Designation"]=Designation
                d["Date of Birth"]=Birth
                l.append(d)
                # k=json.dumps(l,indent=1)
                f1=open("shivani.json","a")
                f1.writelines(l)
                for i in d:
                    print(i,":-",d[i])
                    print("--------xxx---------")
                    print("Congrats",name,"you are  signed")
                
                