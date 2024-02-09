'''
Specifically, write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; if the city name is blank, then
the function prints a report (which I’ll describe) before exiting.
 If the city name isn’t blank, then the program should also ask the user how much
rain has fallen in that city (typically measured in millimeters). After the user enters
the quantity of rain, the program again asks them for a city name, rainfall amount,
and so on—until the user presses Enter instead of typing the name of a city.
 When the user enters a blank city name, the program exits—but first, it reports
how much total rainfall there was in each city
'''

def get_rainfall():
    cities = {}  

    while True:
        city = input("Enter the name of the city or press enter to finish: ")
        if not city:
            break

        rain = input("How much did it rain in mm?: ")
        cities[city] = cities.get(city, 0) + int(rain)

    for city, rain in cities.items():
        print(f"It rained {rain}mm in {city}")



if __name__ == "__main__":
    get_rainfall()