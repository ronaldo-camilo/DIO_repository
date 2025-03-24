def winBalance():
    if(win < 0 or lose < 0):
        return "Invalid value"
    else:
        return win - lose

def level():
    if(winBalance() <= 0):
        level = "Newbie"

    elif(winBalance() > 0 and winBalance() <= 10):
        level = "Iron"
    
    elif(winBalance() > 10 and winBalance() <= 20):
        level = "Brass"
    
    elif(winBalance() > 20 and winBalance() <= 50):
        level = "Silver"
    
    elif(winBalance() > 50 and winBalance() <= 80):
        level = "Gold"
    
    elif(winBalance() > 80 and winBalance() <= 90):
        level = "Diamond" 
    
    elif(winBalance() > 90 and winBalance() <= 100):
        level = "Legend"

    elif(winBalance() > 100):
        level = "Immortal"
    
    return str(level)

print("----------------------------------------------")
print(" ||| Welcome to Ranked Matches Calculator ||| ")
print("----------------------------------------------")

print("Please enter the ammount of Victories:")
win = int(input())

print("Please enter the ammount of Defeats:")
lose = int(input())

print("\nThe Hero has " + str(winBalance()) + " win(s) balance and received the " + str(level()) + " title !")

if(winBalance() <= 0):
    print("\n-----------------------")
    print("||| Keep Trying !!! |||")
    print("-----------------------")
else:
    print("\n--------------------------")
    print("||| Congratulations!!! |||")
    print("--------------------------")



