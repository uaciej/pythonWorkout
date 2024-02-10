'''
Instead of printing just the total rainfall for each city, print the total rainfall and
the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40
for Boston, you would see that the total was 90 and the average was 30
'''

def get_rainfall():
    cities = {}  

    while True:
        city = input("Enter the name of the city or press enter to finish: ")
        if not city:
            break

        rain = input("How much did it rain in mm?: ")
        cities[city] = cities.get(city, [])
        cities[city].append(int(rain))
        print(cities)

    

    for city, rain in cities.items():
        print(f"It rained a total of {sum(rain)}mm and average of {sum(rain)/len(rain)}mm in {city}")



if __name__ == "__main__":
    get_rainfall()