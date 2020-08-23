loginusername="user1";

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
        print(expamt)
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
