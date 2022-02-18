# repository
APPETIZER = ["Calamari = 10 php", "Fries = 10 php", "Hotdog = 15 php", "Dumplings = 20 php"]
ap_price = [10, 10, 15, 20]

MAIN_COURSE = ["Tinola = 249 php", "Pork Sinigang = 249 php", "Bicol Express = 299 php", "Kare-Kare = 299 php"]
mc_price = [249, 249, 299, 299]

DESSERT = ["Special Halo-halo = 99 php", "Leche Flan = 99 php", "Chocolate Cake = 149 php", "Ube Pie = 39 php"]
dess_price = [99, 99, 149, 39]

DRINKS = ["Iced Tea = 29 php", "Coke = 29 php", "Sprite = 69 php", "Buko Juice 39 php"]
dr_price = [29, 29, 69, 39]

foodOrder = []
foodCost = []

print ('''Hello and welcome to Balonso's resto
What would you like to order?

''')

print ('''[1] APPETIZERS
 
[1] Calamari - 10 php
[2] Fries - 10 php
[3] Hotdog - 15 php
[4] Dumplings - 20 php


[2] MAIN COURSE

[1] Tinola - 249 php 
[2] Pork Sinigang  - 249 php
[3] Bicol Express - 299 php
[4] Kare-Kare - 299 php


[3] DESSERTS

[1] Special Halo-halo - 149 php 
[2] Leche Flan  - 149 php
[3] Chocolate Cake  - 149 php
[4] Ube Pie - 39 php


[4] DRINKS

[1] Iced Tea - 29 php 
[2] Coke  - 29 php
[3] Sprite  - 29 php
[4] Buko Juice - 39 php

Select What would you like to order
''')

print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")

order = int(input("Enter the Number: "))
print(" ")
order != 0
while order :
    if order == 1:
        print("What Appetizers would you like to order?")
        print ("[1] Calamari - 10 php ")
        print ("[2] Fries - 10 php")
        print ("[3] Hotdog - 15 php")
        print ("[4] Dumplings - 20 php")
        print ("[0] Type '0' If None")

        app_order = True
        while app_order:
            app_order = input("Enter a number of the Appetizer: ")
            if app_order == "1":
                foodOrder.append(APPETIZER[0])
                foodCost.append(ap_price[0])
            elif app_order == "2":
                foodOrder.append(APPETIZER[1])
                foodCost.append(ap_price[1])
            elif app_order == '3':
                foodOrder.append(APPETIZER[2])
                foodCost.append(ap_price[2])
            elif app_order == '4':
                foodOrder.append(APPETIZER[3])
                foodCost.append(ap_price[3])
            elif app_order == '0':
                app_order = False
                print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                order = int(input("Enter the Number: "))
            else:
                print("Numbers should be 1-4 only")
                done = input('would you still like to order? Y/N: ')
                if done == "Y":
                    app_order = True
                else:
                    app_order = False
                    print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                    order = int(input("Enter the Number: "))
                

    elif order == 2:
        print("What Main Course would you like to order?")
        print ("[1] Tinola - 249 php ")
        print ("[2] Pork Sinigang  - 249 php")
        print ("[3] Bicol Express - 299 php")
        print ("[4] Kare-Kare - 299 php")
        print ("[0] Type '0' If None")

        app_order = True
        while app_order:
            app_order = input("Enter a number of the Main Course: ")
            if app_order == "1":
                foodOrder.append(MAIN_COURSE[0])
                foodCost.append(mc_price[0])
            elif app_order == "2":
                foodOrder.append(MAIN_COURSE[1])
                foodCost.append(mc_price[1])
            elif app_order == "3":
                foodOrder.append(MAIN_COURSE[2])
                foodCost.append(mc_price[2])
            elif app_order == "4":
                foodOrder.append(MAIN_COURSE[3])
                foodCost.append(mc_price[3])
            elif app_order == '0':
                app_order = False
                print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                order = int(input("Enter the Number: "))
            else:
                print("Numbers should be 1-4 only")
                done = input('would you still like to order? Y/N: ')
                if done == "Y":
                    app_order = True
                else:
                    app_order = False 
                    print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                    order = int(input("Enter the Number: "))


    elif order == 3:
        print ("What type of Dessert Would you like to order?")
        print ("[1] Special Halo-halo - 149 php ")
        print ("[2] Leche Flan  - 149 php")
        print ("[3] Chocolate Cake  - 149 php")
        print ("[4] Ube Pie - 39 php")
        print ("[0] Type '0' If None")
        app_order = True
        while app_order :
            app_order = input("Enter a number of the Dessert: ")
            if app_order == "1":
                foodOrder.append(DESSERT[0])
                foodCost.append(dess_price[0])
            elif app_order == "2":
                foodOrder.append(DESSERT[1])
                foodCost.append(dess_price[1])
            elif app_order == "3":
                foodOrder.append(DESSERT[2])
                foodCost.append(dess_price[2])
            elif app_order == "4":
                foodOrder.append(DESSERT[3])
                foodCost.append(dess_price[3])
            elif app_order == '0':
                app_order = False
                print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                order = int(input("Enter the Number: "))
            else:
                print("Numbers should be 1-4 only")
                done = input('would you still like to order? Y/N: ')
                if done == "Y":
                    app_order = True
                else:
                    app_order = False 
                    print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                    order = int(input("Enter the Number: "))


    elif order == 4:
        print ("What Drinks would like to order?")
        print ("[1] Iced Tea - 29 php ")
        print ("[2] Coke  - 29 php")
        print ("[3] Sprite  - 29 php")
        print ("[4] Buko Juice - 39 php")
        print ("[0] Type '0' If None")
        app_order = True
        while app_order :
            app_order = input("Enter a number of the Drinks: ")
            if app_order == "1":
                foodOrder.append(DRINKS[0])
                foodCost.append(dr_price[0])
            elif app_order == "2":
                foodOrder.append(DRINKS[1])
                foodCost.append(dr_price[1])
            elif app_order == "3":
                foodOrder.append(DRINKS[2])
                foodCost.append(dr_price[2])
            elif app_order == "4":
                foodOrder.append(DRINKS[3])
                foodCost.append(dr_price[3])
            elif app_order == '0':
                app_order = False
                print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                order = int(input("Enter the Number: "))
            else:
                print("Numbers should be 1-4 only")
                done = input('would you still like to order? Y/N: ')
                if done == "Y":
                    app_order = True
                else:
                    app_order = False 
                    print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
                    order = int(input("Enter the Number: "))
    else:
        print('Numbers should be 1-4 only ')
        done = input('would you still like to order? Y/N: ')
        if done == "Y":
            print("Select a Number [1] APPETIZERS, [2] MAIN COURSE, [3] DESSERTS, [4] DRINKS", "[0] IF NONE")
            order = int(input("Enter the Number: "))
        else:
            break
        
    

print("Here is the list of your Order")
print ("You ordered: ", *foodOrder, sep="\n")

total = sum(foodCost)
print ("The total amount is:", total, "PHP")

if total >= 0:
    payment = int(input("Please input your payment: "))

    change = int(payment - total) 
    print('The total change is: ', change, "PHP")
    print('Thanks for ordering')

else:
    print('Thanks for ordering')




