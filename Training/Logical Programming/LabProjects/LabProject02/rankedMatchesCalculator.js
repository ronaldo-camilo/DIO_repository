function winBalance(){
    if(win < 0 || lose < 0)
        return "Invalid Value";

    else
        return win - lose;
}

function level(){
    if(winBalance() <= 0)
        level = "Newbie";

    else if(winBalance() > 0 || winBalance() <= 10)
        level = "Iron";

    else if(winBalance() > 10 || winBalance() <= 20)
        level = "Brass";

    else if(winBalance() > 20 || winBalance() <= 50)
        level = "Silver";

    else if(winBalance() > 50 || winBalance() <= 80)
        level = "Gold";

    else if(winBalance() > 80 || winBalance() <= 90)
        level = "Diamond";

    else if(winBalance() < 90 || winBalance() <=100)
        level = "Legend";
    
    else if(winBalance() > 100)
        level = "Immortal";

    return str(level);
}
console.log("Enter the Wins ammount")
let win = parseInt(gets());

console.log("Enter the Lose ammount")
let lose = readInt(gets());

console.log("The Hero has " + str(winBalance()) + " win(s) balance and reached the level " + str(level()) + " !")
