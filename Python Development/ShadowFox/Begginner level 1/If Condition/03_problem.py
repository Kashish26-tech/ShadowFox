# Ceck if two cities belong to the same same country or not

city_country={
    "sydney":"Australia", 
    "melbourne":"Australia", 
    "brisbane":"Australia", 
    "perth":"Australia",
    "dubai":"UAE", 
    "abu dhabi":"UAE", 
    "sharjah":"UAE", 
    "ajman":"UAE",
    "mumbai":"India", 
    "banglore":"India", 
    "chennai":"India",
    "delhi":"India"}

city1=input("Enter a city: ").strip().lower()
city2=input("Enter the another city: ").strip().lower()

if (city_country.get(city1)==city_country.get(city2)):
    print("Both cities are in ",city_country.get(city1))

else:
    print("They don't belong to the same country")