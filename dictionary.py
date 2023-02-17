# student = {"name":{"first_name":"Jak",
#                     "second_name":"Bowes"},
#                      "age": 21,
#                      "city":"Manchester"}
# print(student)

# for key,val in student.items():
#     print(key,"<<item",val,"<<value")

# people = {"names":{"first_name": "john","last_name":"jones", "age": 21, "city": "salford"},
# "baby":{"first_name": "jak","last_name":"bowes","age": 21, "city":"oldham"},
# "sugar":{"first_name": "joe","last_name":"smith","age": 34, "city":"manchester"}}

# for keys in people.values():
#     print(keys)

# cities = {"Manchester" : {"Info" : {"Size" : "2M",
#                                     "Region" : "NW"}},
#                         "London" : {"Info" : {"Size" : "2M",
#                                     "Region" : "SW"}},
#                          "Birmingham" : {"Info" : {"Size" : "2M",
#                                     "Region" : "MD"}}}
# for city in cities.keys():
#     print(city)

# message = ""
# while message != "quit":
#     message = input("prompt")
#     print(message)

# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != "quit":
#         print("  I'll add " + topping + " to your pizza.")
#     else:
#         break

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
