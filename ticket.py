
# age = 11
# ticket_price = 0 

# age = int(input("How old are you?\n"))

# if age < 3:
#     ticket_price = 0 
# elif age >= 3 & age <= 12:
#     ticket_price = 10
# else:
#     ticket_price = 15

# print("Your ticket is: ",ticket_price, "£")

#def function_name():
#   <code>
# def add_number(num1,num2):
# num = num1 % num2
#     print(num1 % num2)

# add_number(3,7)

def greeting(name="David",message="Hi there"):
    print(f"Hello {name}, {message}")


def comparison_function(first_num,sec_num):
    if first_num > sec_num:
        print("Yes")
    else:
        print("No")

comparison_function(7,1)

def division(x,y,z):
    print((x/y)*z)

division(15,5)
