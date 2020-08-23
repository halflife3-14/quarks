
loginusername="user1";
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
    
    

