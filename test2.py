
def adddata(x):
    loginusername=x;

    data = open(loginusername+".txt","r")
    expdata=data.readlines()

    delimit=":";
    register={};
    for eachexp in expdata:
    
        temp=eachexp.split(":")
        temp[1]=temp[1].rstrip('\n')
        temp[1]=int(temp[1])
        register[temp[0]]=temp[1]
        
    prevexp= input("Do you need to view your exp data (y/n):")
    if prevexp == "y":
        for keys in register.keys():
            print(keys,register[keys])
    temp="y";
    while temp=="y":
        temp=input("Do you need to add any other expenditure (y/n):")
        if temp == "y":
            exptype=input("Enter your expenditure type :")
            expamt=int(input("Enter your expenditure amount :"))
            for keys in register.keys():
                if exptype == keys:
                    temp=1;
            
            if temp==1:
                x= register[exptype];
                y= expamt;
                z=x+y;
                register[exptype]=z;
            else:
                register[exptype]=expamt;
    data.close()
    data = open(loginusername+".txt","w") 
    for keys in register.keys():
        print(keys,register[keys])     
    delimt=":";

    for keys1 in register.keys():
        string=[keys1,str(register[keys1])]
        data.write(delimt.join(string))
        data.write("\n")

def signin():
    fhandle= open("Database.txt","a+")
    
    register={};
    with open ("Database.txt","r") as database:
       users=database.readlines()
       for members in users:
        temp=members.split(":")
        register[temp[0]]=temp[1] 
        
    
    username = input("Enter your username :")
    for keys1 in register.keys():
        if username == keys1:
            print("Try a different user name")
            exit()
        
    password = input("Enter your password :")
    delim=":";
    string1 = [username,password]
    collectdata(username)
    print("Login again to see other features")
    fhandle.write("\n")
    x =delim.join(string1)
    fhandle.write(x)
    

def collectdata(x):
    loginusername=x;
    database= open(loginusername+".txt","w")
    exp={};

    exp['Monthly salary']=input("Enter your monthly salary :")
    exp['House rent']=input("Enter your house rent :")
    exp['School fee']=input("Enter your child's school fee :")
    exp['Food']=input("Enter your expenditure on food :")
    exp['Insurance']=input("Enter your expenditure on Insurance :")
    exp['Current bill']=input("Enter your current bill :")
    temp="y";
    while temp=="y":
        temp=input("Do you need to add any other expenditure (y/n):")
        if temp == "y":
            exptype=input("Enter your expenditure type :")
            expamt=input("Enter your expenditure amount :")
            exp[exptype]=expamt;
    delimt=":";

    for keys1 in exp.keys():
        string=[keys1,exp[keys1]]
        database.write(delimt.join(string))
        database.write("\n")

def login():
    register={};
    with open ("Database.txt","r") as database:
       users=database.readlines()
       for members in users:
        temp=members.split(":")
        register[temp[0]]=temp[1]  
        
    username=input("Enter your username :")
    password=input("Enter your password :")
    for keys1 in register.keys():
        if username == keys1:
            if password == register[keys1]:
                print("logged in")
                adddata(username)
                print("Added successfully. Login again to see other features")
                exit()
        

    print("Username or Password error")





euser = input("Are you an existing user (y/n) :")
 
if euser == "y":
    login()
if euser == "n":
    signin()