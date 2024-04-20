'''
 Create a dict whose keys are city names, and whose values are temperatures in
Fahrenheit. Now use a dict comprehension to transform this dict into a new
one, keeping the old keys but turning the values into the temperature in
degrees Celsius.'''


def city_temps_converter(dic):
    return {k : "{:.1f}".format((v - 32) * 5/9) for k, v in dic.items()}



if __name__ == "__main__":
    city_temperatures = {
    "New York": 45,
    "Los Angeles": 68,
    "Chicago": 38,
    "Houston": 72,
    "Phoenix": 80,
    "Philadelphia": 50
}
    print(city_temps_converter(city_temperatures))