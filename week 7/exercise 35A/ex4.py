'''
It’s sometimes useful to transform data from one format into another. 
Download a JSON-formatted list of the 1,000 largest cities in the United States from
http://mng.bz/Vgd0. Using a dict comprehension, turn it into a dict in which
the keys are the city names, and the values are the populations of those cities.
Why are there only 925 key-value pairs in this dict? Now create a new dict, but
set each key to be a tuple containing the state and city. Does that ensure there
will be 1,000 key-value pairs?
'''
import json

def json_dic(json_file):
    return {dic["city"] : dic["population"] for dic in json.load(open(json_file))}
    
def json_dic_tup(json_file):
    return {(dic["city"], dic["state"]) : dic["population"] for dic in json.load(open(json_file))}

    

if __name__ == "__main__":
    print(json_dic('../assets/cities.json'))
    print(json_dic_tup('../assets/cities.json'))