import json
from pprint import pprint

data = {"name" : "morteza", "age" : 29, "city" : "tehran"}

def write_json(data, json_file):
    """
    write data to json_file
    """
    with open(json_file, "w") as target:
        json.dump(data, target)


def read_json(json_file):
    """
    read from json_file
    """
    with open(json_file,  "r") as target:
        json_obj = json.load(target)
    
    return json_obj

if __name__ == "__main__":

    # write_json(data, "test.json")

    pprint(read_json("test.json"))
