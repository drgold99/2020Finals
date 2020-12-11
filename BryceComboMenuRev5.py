def tax(subtotal):
    theTotalAmount=subtotal*(1+7/100)
    theTotalAmount=round(theTotalAmount,2)
    return theTotalAmount
total=0                        #accumulative variable
masterList=[]
inputList=[]
ui="w"
while(ui!="q"):
    sandwhich=input("Please pick a item to order, krabby patty (kp) $1.25, double Krabby patty (dkp) $2.00, triple krabby patty (tkp) $3.00, krabby meal (km) $3.50, double krabby meal (dkm) $3.75, triple krabby meal (tkm) $4.00, salty sea dog (ssd) $1.25, footlong (f) $2.00, sailors surprise (ss) $3.00, golden leaf (gl) $2.00, kelp rings (kr) $1.50, kelp shake (ks) $2.00 ")
    '''print(sandwhich)'''
    if sandwhich=="kp":
        total+=1.25
        masterList.append("krabby patty")
    elif sandwhich=="dkp":
        total+=2
        masterList.append("double krabby patty")
    elif sandwhich=="tkp":
        total+=3
        masterList.append("triple krabby patty")
    elif sandwhich=="km":
        total+=3.50
        masterList.append("krabby meal")
    elif sandwhich=="dkm":
        total+=3.75
        masterList.append("double krabby meal")
    elif sandwhich=="tkm":
        total+=4
        masterList.append("triple krabby meal")
    elif sandwhich=="ssd":
        total+=1.25
        masterList.append("salty sea dog")
    elif sandwhich=="f":
        total+=2
        masterList.append("footlong")
    elif sandwhich=="ss":
        total+=3
        masterList.append("sailors surprise")
    elif sandwhich=="gl":
        total+=2
        masterList.append("golden loaf")
        ui=input("Do you want sauce with it y or n? It cost $2.50 ")
        if ui=="y":
            total+=2.50
            masterList.append("sauce")
    elif sandwhich=="kr":
        total+=1.50
        masterList.append("kelp rings")
        ui=input("Do you want salty sauce on it y or n? It cost $0.50 ")
        if ui=="y":
            total+=.50
            masterList.append("salty sauce")
    elif sandwhich=="ks":
        total+=2
        masterList.append("kelp shake")
    if sandwhich=="kp" or sandwhich=="dkp" or sandwhich=="tkp":
        print("if you pick krabby patty, sea cheese cost is $1.50\nif you pick double krabby patty, sea cheese cost is $2.25\nif you pick triple krabby patty, sea cheese cost is $3.25 ")
        ui=input("Do you want sea cheese on it? y or n ")
        if ui=="y":
            masterList.append("sea cheese")
            if sandwhich=="kp":
                    total+=1.50
            elif sandwhich=="dkp":
                    total+=2.25
            elif sandwhich=="tkp":
                    total+=3.25
    beverage=input("would you like a seafoam soda, y or n? ")
    if (beverage=="y"):
        beverage=input("s for $1.00, m for $1.25, l for $1.50 ")
        '''print("you said",beverage,"drink.")'''
        if beverage=="s":
            total+=1
            inputList.append("small")
        elif beverage=="m":
            total+=1.25
            inputList.append("medium")
        elif beverage=="l":
            total+=1.50
            inputList.append("large")
        masterList.append("seafoam soda")
    fries=input("Would you like coral bits, y or n? ")
    if(fries=="y"):
        fries=input("Would you like a s for $1.00, m for $1.25, or l for $1.50? ")
        if (fries=="s"):
            total+=1
            inputList.append("small")
        elif (fries=="m"):
            total+=1.25
            inputList.append("medium")
        elif (fries=="l"):
            total+=1.50
            inputList.append("large")
        masterList.append("coral bits")
    ui=input("type in q when you are done ordering. ")
'''total=('${:,.2f}'.format(total))'''
masterList.append(inputList)
print(masterList)
print("your order is:")
for i in range(len(masterList)):
    print(masterList[i])
    
print("the sub total is",total)
print("the total is",tax(total))