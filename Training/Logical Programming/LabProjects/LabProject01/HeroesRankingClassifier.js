console.log("-----------------------------------");
console.log("||| Welcome to the Hero Ranking |||");
console.log("-----------------------------------");

let heroName = ["Archer", "Warrior", "Mage", "Assassin", "Tank", "Support", "Marksman"];


let heroRanking;

for(let i = 0; i < heroName.length; i++){
	
    let heroXP = Math.floor(Math.random() * 11001);

	if(heroXP <= 1000)
      heroRanking = "Iron";

    else if(heroXP > 1000 && heroXP <= 2000)
      heroRanking = "Brass";

    else if(heroXP > 2000 && heroXP <= 5000)
      heroRanking = "Silver";

    else if(heroXP > 5000 && heroXP <= 7000)
      heroRanking = "Gold";

    else if(heroXP > 7000 && heroXP <= 8000)
      heroRanking = "Platinum";

    else if(heroXP > 8000 && heroXP <= 9000)
      heroRanking = "Rising";

    else if(heroXP > 9000 && heroXP <= 10000)
      heroRanking = "Immortal";

    else if(heroXP > 10000)
      heroRanking = "Shinning";

    else
      heroRanking = "Not Ranked";

    console.log("The Hero called " + heroName[i] + " ranking level is " + heroRanking + " with " + heroXP + " XP");
}