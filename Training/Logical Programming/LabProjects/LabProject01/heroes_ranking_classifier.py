# 1st code

'''
print("Insert the hero's name:")
hero_name = str(input())

print("Insert the XP amount:")
xp_amount = int(input()) 

if(xp_amount <= 1000):
    str(print("Iron"))

elif(xp_amount > 1000 and xp_amount <= 2000):
    str(print("Brass"))

elif(xp_amount > 2000 and xp_amount <= 5000):
    str(print("Silver"))

elif(xp_amount > 5000 and xp_amount <= 7000):
    str(print("Gold"))

elif(xp_amount > 7000 and xp_amount <= 8000):
    str(print("Platinum"))

elif(xp_amount > 8000 and xp_amount <= 9000):
    str(print("Ascendent"))

elif(xp_amount > 9000 and xp_amount <= 10000):
    str(print("Immortal"))

elif(xp_amount > 10000):
    str(print("Shinning"))

'''

# 2nd Code

'''
print("Welcome to the Heroes Ranking")
print("-----------------------------")

print("Please enter the Hero's Name")
hero_name = str(input())

print("Please enter the Hero's XP Ammount")
xp_ammount = int(input())

#ranking = str(0)

if(xp_ammount <= 0):
    ranking = str("Noob")

elif(xp_ammount > 0 and xp_ammount <= 1000):
    ranking = str("Iron")

elif(xp_ammount > 1000 and xp_ammount <= 2000):
    ranking = str("Brass")

elif(xp_ammount > 2000 and xp_ammount <= 5000):
    ranking = str("Silver")

elif(xp_ammount > 5000 and xp_ammount <= 7000):
    ranking = str("Gold")

elif(xp_ammount > 7000 and xp_ammount <= 8000):
    ranking = str("Platinum") 

elif(xp_ammount > 8000 and xp_ammount <= 9000):
    ranking = str("Rising")

elif(xp_ammount > 9000 and xp_ammount <= 10000):
    ranking = str("Immortal")

elif(xp_ammount > 10000):
    ranking = str("Shinning")

print("The Heroes Ranking for " + hero_name + " is " + ranking)
print("Congratulations!!!")

'''

# 3rd Code

'''
print("---------------------------------")
print("||| Welcome to Heroes Ranking |||")
print("---------------------------------")
print("")

print("Please enter the Hero's name:")
hero_name = str(input())
print("Please enter the Hero's XP ammount:")
xp_ammount = int(input())

if(xp_ammount <= 0):
    ranking = str("Newbie")

elif(xp_ammount > 0 and xp_ammount <= 1000):
    ranking = str("Iron")

elif(xp_ammount > 1000 and xp_ammount <= 2000):
    ranking = str("Brass")

elif(xp_ammount > 2000 and xp_ammount <= 5000):
    ranking = str("Silver")

elif(xp_ammount > 5000 and xp_ammount <= 7000):
    ranking = str("Gold")

elif(xp_ammount > 7000 and xp_ammount <= 8000):
    ranking = str("Platinum") 

elif(xp_ammount > 8000 and xp_ammount <= 9000):
    ranking = str("Rising")

elif(xp_ammount > 9000 and xp_ammount <= 10000):
    ranking = str("Immortal")

elif(xp_ammount > 10000):
    ranking = str("Shinning")

print("")
print("The Heroes Ranking for " + hero_name + " is " + ranking)
print("")

print("--------------------------")
if(xp_ammount <= 0):
    print("You need to trainning a little more... ")

else:
    print("||| Congratulations!!! |||")
    
print("--------------------------")

'''

# Final Code

def lvl_ranking():

    if(xp_ammount <= 0):
        ranking = "Newbie"

    elif(xp_ammount > 0 and xp_ammount <= 1000):
        ranking = "Iron"

    elif(xp_ammount > 1000 and xp_ammount <= 2000):
        ranking = "Brass"

    elif(xp_ammount > 2000 and xp_ammount <= 5000):
        ranking = "Silver"

    elif(xp_ammount > 5000 and xp_ammount <= 7000):
        ranking = "Gold"

    elif(xp_ammount > 7000 and xp_ammount <= 8000):
        ranking = "Platinum" 

    elif(xp_ammount > 8000 and xp_ammount <= 9000):
        ranking = "Rising"

    elif(xp_ammount > 9000 and xp_ammount <= 10000):
        ranking = "Immortal"

    elif(xp_ammount > 10000):
        ranking = "Shinning"
    
    return str(ranking)

print("---------------------------------")
print("||| Welcome to Heroes Ranking |||")
print("---------------------------------")

print("\nPlease enter the Hero's name:")
hero_name = str(input())
print("Please enter the Hero's XP ammount:")
xp_ammount = int(input())

print("\nThe Heroes Ranking for " + hero_name + " is " + lvl_ranking())

print("\n--------------------------")
if(xp_ammount <= 0):
    print("||| You need to training a little more... |||")
else:
    print("||| Congratulations!!! |||")
    
print("--------------------------")