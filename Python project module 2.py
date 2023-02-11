# -*- coding: utf-8 -*-
#%% Master list of properties


#%% PROPERTY TYPE SELECTION
print('''
-------------------------------------------------------------------------------
Option A = HDB
Option B = Condominium      
-------------------------------------------------------------------------------  
     ''')
option_choose=str.upper(input("Please input Option: "))

while True :
    try:
        option_choose == ("A","B")                   #see if can create while loop
        if option_choose=="A" :
            property_type= "HDB"
            print(f"The property you have chosen is {property_type}")
            choice_1=str.upper(input("Do you wish to continue? [Y/N]: "))
            if choice_1 == "Y" :
                    break
        elif option_choose =="B" :
            property_type= "Condo"
            print(f"The property you have chosen is {property_type}")
            choice_1=str.upper(input("Do you wish to continue? [Y/N]: "))
            if choice_1 == "Y" :
                    break
            elif choice_1 == "N" :
                print("Please Re-enter your choice")
    except ValueError :
        print("The option you chose is invalid, please re-enter!")
        
#%% budget

while True:
    try: 
        budget= float(input("Please Input your budget amount: "))
        if budget > 0 :
            choice_2= input(f"Your budget is ${budget}, do you wish to continue? [Y/N]: ")
            if choice_2== "Y":
                    break
            elif choice_2 == "N" : 
                budget= float(input("Please re-enter your budget amount: ")) 
        break
    except ValueError :
        print("The value you have inserted is invalid, please try again! ")
  
  
    
#NEED TO LOOP 0 VALUES ERROR PROMPT
    
#%% LOCATION SELECTOR
print('''
|Let's Pick Your New home Location!|
-------------------------------------------------------------------------------
Option A = North
Option B = North East
Option C = East
Option D = South East
Option E = South
Option F = South West
Option G = West
Option H = North West
-------------------------------------------------------------------------------
      ''')
location_variable= str.upper(input("Please input an option from the choices above:"))

#%% MRT BRANCHING (WHICH MRT DO USERS GET TO PICK)
if location_variable=="A":
    print('''
-------------------------------------------------------------------------------          
          Here Are The available MRT's:
          Option A =
          Option B =
          Option C =
-------------------------------------------------------------------------------   
          ''')
    mrt_location=input("Please pick one option from above: ")

#%% Room size sqft
room_size= int(input("Please input the size of the room you would like in sqft: "))









#%% Number of bedrooms
print('''
-------------------------------------------------------------------------------
| Here are the number of bedrooms available! |
2 bedroom
3 bedroom
4 bedroom
5 bedroom    
-------------------------------------------------------------------------------
      ''')
      
number_of_room= int(input("Please input the number of rooms you want from 2 - 5: "))      