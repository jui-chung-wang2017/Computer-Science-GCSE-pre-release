'''
Copyright (C)  2/2020  Ray Wang
Python Code for IGCSE 2020 pre-release Task 2

'''


#parallel arrays
item_number = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
category = ["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet", "Tablet", "Tablet", "Tablet", "SIM Card", "SIM Card", "Case", "Case", "Charger", "Charger"]
description = ["Compact Phone", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 256 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Tab Deluxe - 10-inch screen and 256 GB memory", "SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)", "Standard Case", "Luxury Case", "Car Charger", "Home Charger"]
itemcode = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"]
price = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99, 0.00, 9.99, 0.00, 50.00, 19.99, 15.99]
basket = [" ", " ", " ", " ", " "]
basketNum = [" ", " ", " ", " ", " "]
basketCost = 0
choiceNum = 0


inputValidator = False
while inputValidator == False:

#phones
    buyChoice = input("Would you like to purchase a phone or a tablet? \n")
    buyChoice = buyChoice.lower()
    if buyChoice == "phone":
        print("The phones available are: \n")
        for i in range(0,6):
            print(item_number[i], "  ", description[i], " £", price[i])
        basketNum[0] = int(input("Please enter the item number to add to your basket: \n--"))
        while inputValidator == False:
            if 1 <= basketNum[0] <= 16:
                while inputValidator == False:
                    for j in item_number:
                        if j == basketNum[0]:
                            choiceNum = j-1
                    if category[choiceNum] == "Phone":
                        basketCost = basketCost + price[choiceNum]
                        basket[0] = description[choiceNum]
                        inputValidator = True
                    
                    else:
                        basketNum[0] = int(input("01 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    inputValidator = True
            elif basketNum[0] == 0:
                basketNum[0] = int(input("00 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
            else:
                basketNum[0] = int(input("00 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

    
        print("Item added succesfully")
        print("The current item(s) in your basket: \n")
        print(*basket, sep = "\n")    
        print("\nYour running total is: ", basketCost, "\n")
        print("-----------------------------------------------------------------------------")


#tablets
    elif buyChoice == "tablet":
        print("The tablets available are: \n")
        for i in range(6,10):
            print(item_number[i], "  ", description[i], " £", price[i])
        basketNum[0] = int(input("Please enter the item number to add to your basket: \n--"))
        while inputValidator == False:
            if 1 <= basketNum[0] <= 16:
                while inputValidator == False:
                    for j in item_number:
                        if j == basketNum[0]:
                            choiceNum = j-1
                    if category[choiceNum] == "Tablet":
                        basketCost = basketCost + price[choiceNum]
                        basket[0] = description[choiceNum]
                        inputValidator = True
                    
                    else:
                        basketNum[0] = int(input("03 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    inputValidator = True
            elif basketNum[0] == 0:
                basketNum[0] = int(input("02 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
            else:
                basketNum[0] = int(input("02 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
        print("Item added succesfully")
        print("The current item(s) in your basket: \n")
        print(*basket, sep = "\n")
        print("\nYour running total is: ", basketCost, "\n")
        print("-----------------------------------------------------------------------------")
        
    else:
        print("That item is currently unavailable")


#sim cards
inputValidator = False
while inputValidator == False:
    print("The SIM cards available are: \n")
    for i in range(10,12):
        print(item_number[i], "  ", description[i], " £", price[i])
    basketNum[1] = int(input("Please enter the item number to add to your basket: \n--"))
    while inputValidator == False:
        if 1 <= basketNum[1] <= 16:
            while inputValidator == False:
                for j in item_number:
                    if j == basketNum[1]:
                        choiceNum = j-1
                if category[choiceNum] == "SIM Card":
                    basketCost = basketCost + price[choiceNum]
                    basket[1] = description[choiceNum]
                    inputValidator = True
                    
                else:
                    basketNum[1] = int(input("05 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                inputValidator = True
        elif basketNum[1] == 0:
            basketNum[1] = int(input("04 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
        else:
            basketNum[1] = int(input("04 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))


    print("Item added succesfully")
    print("The current item(s) in your basket: \n")
    print(*basket, sep = "\n")
    print("\nYour running total is: ", basketCost, "\n")
    print("-----------------------------------------------------------------------------")

#cases
inputValidator = False
while inputValidator == False:
    caseChoice = input("Would you like a case? \n")
    caseChoice = caseChoice.lower()
    if caseChoice == "yes":
        print("The cases available are: \n")
        for i in range(12,14):
            print(item_number[i], "  ", description[i], " £", price[i])
        basketNum[2] = int(input("Please enter the item number to add to your basket: \n--"))
        while inputValidator == False:
            if 1 <= basketNum[2] <= 16:
                while inputValidator == False:
                    for j in item_number:
                        if j == basketNum[2]:
                            choiceNum = j-1
                    if category[choiceNum] == "Case":
                        basketCost = basketCost + price[choiceNum]
                        basket[2] = description[choiceNum]
                        inputValidator = True
                    
                    else:
                        basketNum[2] = int(input("07 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    inputValidator = True
            elif basketNum[2] == 0:
                basketNum[2] = int(input("06 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
            else:
                basketNum[2] = int(input("06 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
        print("Item added succesfully")
        print("The current item(s) in your basket: \n")
        print(*basket, sep = "\n")
        print("\nYour running total is: ", basketCost, "\n")
        print("-----------------------------------------------------------------------------")

    elif caseChoice =="no":
        inputValidator = True

    else:
        print("Please answer with yes or no")


#chargers
inputValidator = False
while inputValidator == False:
    chargerChoice = input("Would you like a charger? \n")
    chargerChoice = chargerChoice.lower()
    if chargerChoice == "yes":
        while inputValidator == False:
            print("The chargers available are: \n")
            for i in range(14,16):
                print(item_number[i], "  ", description[i], " £", price[i])
            basketNum[3] = int(input("Please enter the item number to add to your basket: \n--"))
            while inputValidator == False:
                if 1 <= basketNum[3] <= 16:
                    while inputValidator == False:
                        for j in item_number:
                            if j == basketNum[3]:
                                choiceNum = j-1
                        if category[choiceNum] == "Charger":
                            basketCost = basketCost + price[choiceNum]
                            basket[3] = description[choiceNum]
                            inputValidator = True
                    
                        else:
                            basketNum[3] = int(input("09 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                        inputValidator = True
                elif basketNum[3] == 0:
                    basketNum[3] = int(input("08 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                else:
                    basketNum[3] = int(input("08 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
            print("Item added succesfully")
            print("The current item(s) in your basket: \n")
            print(*basket, sep = "\n")
            print("\nYour running total is: ", basketCost, "\n")
            print("-----------------------------------------------------------------------------")
            
        inputValidator = False
        while inputValidator == False:
            chargerChoice = input("Would you like an additional charger? \n")
            chargerChoice = chargerChoice.lower()
            if chargerChoice == "yes":
                print("The chargers available are: \n")
                for i in range(14,16):
                    print(item_number[i], "  ", description[i], " £", price[i])
                basketNum[4] = int(input("Please enter the item number to add to your basket: \n--"))
                while inputValidator == False:
                    if 1 <= basketNum[4] <= 16:
                        while inputValidator == False:
                            for j in item_number:
                                if j == basketNum[4]:
                                    choiceNum = j-1
                            if category[choiceNum] == "Charger":
                                basketCost = basketCost + price[choiceNum]
                                basket[4] = description[choiceNum]
                                inputValidator = True
                        
                            else:
                                basketNum[4] = int(input("11 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                            inputValidator = True
                    elif basketNum[4] == 0:
                        basketNum[4] = int(input("10 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    else:
                        basketNum[4] = int(input("10 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
                print("Item added succesfully")
                print("The current item(s) in your basket: \n")
                print(*basket, sep = "\n")
                print("\nYour running total is: ", basketCost, "\n")
                print("-----------------------------------------------------------------------------")

            elif chargerChoice == "no":
                inputValidator = True

            else:
                print("Please answer with yes or no")
            

    elif chargerChoice == "no":
        inputValidator = True

    else:
        print("Please answer with yes or no")



























extendedDeviceBasket = []
extendedDeviceNum = []
extendedSimBasket = []
extendedSimNum = []
extendedCaseBasket = []
extendedCaseNum = []
extendedChargerBasket = []
extendedChargerNum = []
extendedExtraChargerBasket = []
extendedExtraChargerNum = []
extraDeviceCounter = 0




#to purchase more devices

inputValidator = False
while inputValidator == False:
    morePhones = input("Would you like to purchase additional devices? \n")
    morePhones = morePhones.lower()
    if morePhones == "yes":

        inputValidator = False
        while inputValidator == False:

            #phones
            buyChoice = input("Would you like to purchase a phone or a tablet? \n")
            buyChoice = buyChoice.lower()
            if buyChoice == "phone":
                print("The phones available are: \n")
                for i in range(0,6):
                    print(item_number[i], "  ", description[i], " £", price[i])
                extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
                extendedDeviceNum.append(extendedInput)
                extendedDeviceBasket.append(extendedInput)
                while inputValidator == False:
                    if 1 <= extendedDeviceNum[extraDeviceCounter] <= 16:
                        while inputValidator == False:
                            for j in item_number:
                                if j == extendedDeviceNum[extraDeviceCounter]:
                                    choiceNum = j-1
                            if category[choiceNum] == "Phone":
                                basketCost = basketCost + price[choiceNum]
                                extendedDeviceBasket[extraDeviceCounter] = description[choiceNum]
                                basket.append(extendedDeviceBasket[extraDeviceCounter])
                                inputValidator = True
                    
                            else:
                                extendedInput = int(input("13 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                            inputValidator = True
                    elif extendedDeviceNum[extraDeviceCounter] == 0:
                        extendedInput = int(input("12 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    else:
                        extendedInput = int(input("12 This item is not a phone or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

    
                print("Item added succesfully")
                print("The current item(s) in your basket: \n")
                print(*basket, sep = "\n")
                print("\nYour running total is: ", basketCost, "\n")
                print("-----------------------------------------------------------------------------")



        #tablets
            elif buyChoice == "tablet":
                print("The tablets available are: \n")
                for i in range(6,10):
                    print(item_number[i], "  ", description[i], " £", price[i])
                extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
                extendedDeviceNum.append(extendedInput)
                extendedDeviceBasket.append(extendedInput)
                while inputValidator == False:
                    if 1 <= extendedDeviceNum[extraDeviceCounter] <= 16:
                        while inputValidator == False:
                            for j in item_number:
                                if j == extendedDeviceNum[extraDeviceCounter]:
                                    choiceNum = j-1
                            if category[choiceNum] == "Tablet":
                                basketCost = basketCost + price[choiceNum]
                                extendedDeviceBasket[extraDeviceCounter] = description[choiceNum]
                                basket.append(extendedDeviceBasket[extraDeviceCounter])
                                inputValidator = True
                            
                            else:
                                extendedInput = int(input("15 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                            inputValidator = True
                    elif extendedDeviceNum[extraDeviceCounter] == 0:
                        extendedInput = int(input("14 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    else:
                        extendedInput = int(input("14 This item is not a tablet or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
                print("Item added succesfully")
                print("The current item(s) in your basket: \n")
                print(*basket, sep = "\n")
                print("\nYour running total is: ", basketCost, "\n")
                print("-----------------------------------------------------------------------------")
        
            else:
                print("That item is currently unavailable")


        #sim cards
        inputValidator = False
        while inputValidator == False:
            print("The SIM cards available are: \n")
            for i in range(10,12):
                print(item_number[i], "  ", description[i], " £", price[i])
            extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
            extendedSimNum.append(extendedInput)
            extendedSimBasket.append(extendedInput)
            while inputValidator == False:
                if 1 <= extendedSimNum[extraDeviceCounter] <= 16:
                    while inputValidator == False:
                        for j in item_number:
                            if j == extendedSimNum[extraDeviceCounter]:
                                choiceNum = j-1
                        if category[choiceNum] == "SIM Card":
                            basketCost = basketCost + price[choiceNum]
                            extendedSimBasket[extraDeviceCounter] = description[choiceNum]
                            basket.append(extendedSimBasket[extraDeviceCounter])
                            inputValidator = True
                    
                        else:
                            extendedInput = int(input("17 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                        inputValidator = True
                elif extendedSimNum[extraDeviceCounter] == 0:
                    extendedInput = int(input("16 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                else:
                    extendedInput = int(input("16 This item is not a SIM card or is unavlailable. Please enter a valid item number to add to your basket: \n--"))


            print("Item added succesfully")
            print("The current item(s) in your basket: \n")
            print(*basket, sep = "\n")
            print("\nYour running total is: ", basketCost, "\n")
            print("-----------------------------------------------------------------------------")

        #cases
        inputValidator = False
        while inputValidator == False:
            caseChoice = input("Would you like a case? \n")
            caseChoice = caseChoice.lower()
            if caseChoice == "yes":
                print("The cases available are: \n")
                for i in range(12,14):
                    print(item_number[i], "  ", description[i], " £", price[i])
                extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
                extendedCaseNum.append(extendedInput)
                extendedCaseBasket.append(extendedInput)
                while inputValidator == False:
                    if 1 <= extendedCaseNum[extraDeviceCounter] <= 16:
                        while inputValidator == False:
                            for j in item_number:
                                if j == extendedCaseNum[extraDeviceCounter]:
                                    choiceNum = j-1
                            if category[choiceNum] == "Case":
                                basketCost = basketCost + price[choiceNum]
                                extendedCaseBasket[extraDeviceCounter] = description[choiceNum]
                                basket.append(extendedCaseBasket[extraDeviceCounter])
                                inputValidator = True
                    
                            else:
                                extendedinput = int(input("19 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                            inputValidator = True
                    elif extendedCaseNum[extraDeviceCounter] == 0:
                        extendedInput = int(input("18 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                    else:
                        extendedInput = int(input("18 This item is not a case or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
                print("Item added succesfully")
                print("The current item(s) in your basket: \n")
                print(*basket, sep = "\n")
                print("\nYour running total is: ", basketCost, "\n")
                print("-----------------------------------------------------------------------------")

            elif caseChoice =="no":
                extendedCaseNum.append("null")
                extendedCaseBasket.append("No Case")
                inputValidator = True

            else:
                print("Please answer with yes or no")


        #chargers
        inputValidator = False
        while inputValidator == False:
            chargerChoice = input("Would you like a charger? \n")
            chargerChoice = chargerChoice.lower()
            if chargerChoice == "yes":
                while inputValidator == False:
                    print("The chargers available are: \n")
                    for i in range(14,16):
                        print(item_number[i], "  ", description[i], " £", price[i])
                    extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
                    extendedChargerNum.append(extendedInput)
                    extendedChargerBasket.append(extendedInput)
                    while inputValidator == False:
                        if 1 <= extendedChargerNum[extraDeviceCounter] <= 16:
                            while inputValidator == False:
                                for j in item_number:
                                    if j == extendedChargerNum[extraDeviceCounter]:
                                        choiceNum = j-1
                                if category[choiceNum] == "Charger":
                                    basketCost = basketCost + price[choiceNum]
                                    extendedChargerBasket[extraDeviceCounter] = description[choiceNum]
                                    basket.append(extendedChargerBasket[extraDeviceCounter])
                                    inputValidator = True
                    
                                else:
                                    extendedInput = int(input("21 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                                inputValidator = True
                        elif extendedChargerNum[extraDeviceCounter] == 0:
                            extendedInput = int(input("20 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                        else:
                            extendedInput = int(input("20 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
                    print("Item added succesfully")
                    print("The current item(s) in your basket: \n")
                    print(*basket, sep = "\n")
                    print("\nYour running total is: ", basketCost, "\n")
                    print("-----------------------------------------------------------------------------")
            
                inputValidator = False
                while inputValidator == False:
                    chargerChoice = input("Would you like an additional charger? \n")
                    chargerChoice = chargerChoice.lower()
                    if chargerChoice == "yes":
                        print("The chargers available are: \n")
                        for i in range(14,16):
                            print(item_number[i], "  ", description[i], " £", price[i])
                        extendedInput = int(input("Please enter the item number to add to your basket: \n--"))
                        extendedExtraChargerNum.append(extendedInput)
                        extendedExtraChargerBasket.append(extendedInput)
                        while inputValidator == False:
                            if 1 <= extendedExtraChargerNum[extraDeviceCounter] <= 16:
                                while inputValidator == False:
                                    for j in item_number:
                                        if j == extendedExtraChargerNum[extraDeviceCounter]:
                                            choiceNum = j-1
                                    if category[choiceNum] == "Charger":
                                        basketCost = basketCost + price[choiceNum]
                                        extendedExtraChargerBasket[extraDeviceCounter] = description[choiceNum]
                                        basket.append(extendedExtraChargerBasket[extraDeviceCounter])
                                        inputValidator = True
                    
                                    else:
                                        extendedInput = int(input("23 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                                    inputValidator = True
                            elif extendedExtraChargerNum[extraDeviceCounter] == 0:
                                extendedInput = int(input("22 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))
                            else:
                                extendedInput = int(input("22 This item is not a charger or is unavlailable. Please enter a valid item number to add to your basket: \n--"))

        
                        print("Item added succesfully")
                        print("The current item(s) in your basket: \n")
                        print(*basket, sep = "\n")
                        print("\nYour running total is: ", basketCost, "\n")
                        print("-----------------------------------------------------------------------------")

                    elif chargerChoice == "no":
                        inputValidator = True
                        extendedExtraChargerNum.append("null")
                        extendedExtraChargerBasket.append("No additional charger")

                    else:
                        print("Please answer with yes or no")
                        

            elif chargerChoice == "no":
                inputValidator = True
                extendedExtraChargerNum.append("null")
                extendedExtraChargerBasket.append("No additional charger")
                extendedChargerNum.append("null")
                extendedChargerBasket.append("No additional charger")

            else:
                print("Please answer with yes or no")

        inputValidator = False
        extraDeviceCounter =+ 1


    elif morePhones == "no":
        inputValidator = True

    else:
        print("Please answer with yes or no")



    
