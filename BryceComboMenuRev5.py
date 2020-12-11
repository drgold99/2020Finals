def tax(subtotal):
    theTotalAmount=subtotal*(1+7/100)
    theTotalAmount=round(theTotalAmount,2)
    return theTotalAmount
total=0                           #accumulative variable
masterList=[]
def order(total):
    ui="w"
    while(ui!="q"):
        sandwhich=input("Please pick a item to order, krabby patty (kp) $1.25, double Krabby patty (dkp) $2.00, triple krabby patty (tkp) $3.00, krabby meal (km) $3.50, double krabby meal (dkm) $3.75, triple krabby meal (tkm) $4.00, salty sea dog (ssd) $1.25, footlong (f) $2.00, sailors surprise (ss) $3.00, golden leaf (gl) $2.00, kelp rings (kr) $1.50, kelp shake (ks) $2.00 ")
        '''print(sandwhich)'''
        if sandwhich=="kp":
            sandwhich="krabby patty"
            total+=1.25
            masterList.append(sandwhich)
        elif sandwhich=="dkp":
            sandwhich="double krabby patty"
            total+=2
            masterList.append(sandwhich)
        elif sandwhich=="tkp":
            sandwhich="triple krabby patty"
            total+=3
            masterList.append(sandwhich)
        elif sandwhich=="km":
            sandwhich="krabby meal"
            total+=3.50
            masterList.append(sandwhich)
        elif sandwhich=="dkm":
            total+=3.75
            sandwhich="double krabby meal"
            masterList.append(sandwhich)
        elif sandwhich=="tkm":
            sandwhich="triple krabby meal"
            total+=4
            masterList.append(sandwhich)
        elif sandwhich=="ssd":
            sandwhich="salty sea dog"
            total+=1.25
            masterList.append(sandwhich)
        elif sandwhich=="f":
            sandwhich="footlong"
            total+=2
            masterList.append(sandwhich)
        elif sandwhich=="ss":
            sandwhich="sailors surprise"
            total+=3
            masterList.append(sandwhich)
        elif sandwhich=="gl":
            sandwhich="golden loaf"
            total+=2
            masterList.append(sandwhich)
            ui=input("Do you want sauce with it y or n? It cost $2.50 ")
            if ui=="y":
                total+=2.50
                masterList.append("sauce")
            elif sandwhich=="kr":
                sandwhich="kelp rings"
                total+=1.50
                masterList.append(sandwhich)
                ui=input("Do you want salty sauce on it y or n? It cost $0.50 ")
            if ui=="y":
                total+=.50
                masterList.append("salty sauce")
            elif sandwhich=="ks":
                sandwhich="kelp shake"
                total+=2
                masterList.append(sandwhich)
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
                beverage="small"
                masterList.append(beverage)
            elif beverage=="m":
                total+=1.25
                beverage="medium"
                masterList.append(beverage)
            elif beverage=="l":
                total+=1.50
                beverage="large"
                masterList.append(beverage)
            masterList.append("seafoam soda")
        fries=input("Would you like coral bits, y or n? ")
        if(fries=="y"):
            fries=input("Would you like a s for $1.00, m for $1.25, or l for $1.50? ")
            if (fries=="s"):
                total+=1
                fries="small"
                masterList.append(fries)
            elif (fries=="m"):
                total+=1.25
                fries="medium"
                masterList.append(fries)
            elif (fries=="l"):
                total+=1.50
                fries="large"
                masterList.append(fries)
            masterList.append("coral bits")
        ui=input("type in q when you are done ordering. ")
        #print("yo're total is",total)
        '''total=('${:,.2f}'.format(total))'''
        #print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4}'.format(sandwhich,beverage,fries,ketchup,total))
order(total)
print("your order is:")
for i in range(masterList):
    print(masterList[i])
    i+1
print("the total is",tax(total))