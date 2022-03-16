from unittest import result


def to_fahrenheit(temp_in_c):
    if(type(temp_in_c) == int or type(temp_in_c) == float):
        result = temp_in_c * 1.8 + 32
        return(result)
    else:
        return(None)


def string_length(string1):
    if(type(string1) == str):
        result = 0
        for i in string1:
            result += 1
        return(result)
    else:
        return(None)
    
    
def sorted_minmax(list1):
    if(type(list1) == list):
        list1 = list(set(list1))
        list1.sort()
        result = (list1, list1[0], list1[-1])
        return(result)
    else:
        return(None)


print(sorted_minmax([3,1,1,2]))


import requests
import json

def derive(equasion):
    url = "https://newton.vercel.app/api/v2/derive/"
    response = requests.get(f"{url}{equasion}")
    result = json.loads(response.text)["result"]
    return(result)

print(derive("x^2+2x"))