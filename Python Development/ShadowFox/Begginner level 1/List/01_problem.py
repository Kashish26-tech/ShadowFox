justice_league = ["Superman", "Batman", "Wonder Women", "Flash", "Aquaman", "Green Lantern"]

#For number of members in list
members=len(justice_league)
print("The number of members in the Justice League is",members)

#Add new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

#Add new leader at beginnig
justice_league.pop(2)     #removes Wonder women
justice_league.insert(0,"Wonder Women")
print(justice_league)

#Insert between two elements
justice_league.remove("Green Lantern")
justice_league.insert(4,"Green lantern") #Index of flash+1=4
print(justice_league)

#New team
num=len(justice_league)
justice_league[0:num]=["Cyborg", "Shazam", "Hawkgirl", "Martian", "Manhunter", "Green Arrow"]
print("New List is..")
print(justice_league)

#Sort aphabetically
justice_league.sort()
print("The sorted list is..")
print(justice_league)

name=justice_league[0]
print("The hero of Justice League is",name)