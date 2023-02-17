student = {"name":"Ibrahim",
           "location":"Manchester",
            "height": 185,
            "food":("Cheese","Chicken"),
            "favourite_colour":["blue","green", 
                               {"shade_of_colour":"teal",
                               "type":"Primary"},
                               {"faded":True}],
            "address":{"street":"123 Generation Street",
            "post_code":"OL1 345",
            "city":"Manchester"}}

student["food"] = ("Cheese","Burger")
print(student["food"])

# student["favourite_colour"][3]["faded"] = False
# print(student["favourite_colour"] # changes faded to false

# student["location"] = "London" # changes location to London
# print(student["location"]) 
# print(student["favourite_colour"])
# print(student["favourite_colour"][2]["shade_of_colour"])        
# print(student["favourite_colour"][-1]["faded"])  


# addr = student["address"] # how to print a specfic part of a dict inside a dict
# print(addr["post_code"])
