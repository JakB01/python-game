#range(start,end,step)
# numbers = list(range(1,56,4)) #goes from (a)) to (b) in steps of (c)
# print(numbers)

# numbers = list(range(0,20,2))
# new_numbers = []

# for square in numbers:
#     new_numbers.append(square**2)
# print(numbers)
# print(new_numbers)


# numbers = [1,2,3,4,5]
# print(numbers)
# num = []
# for i in numbers:
#     num.append(i)
# print(num)

# [<result> for iterator in <list>]
# loop [i**2 for i in range[6]]
# print(loop)
#print cube of a list of odd numbers 1-10 

# lp = list(range(20))
# cubes = [ odd_number*odd_number*odd_number for odd_number in range (1,10,2)]
# print(cubes)

# list = list(list(range(1,10,2)))
# print(list)
# new_list = [i**3 for i in list]
# print(new_list)

# [<result> for iterator in <list>]
loop = [(i % 3)**2 for i in range (10,21)]
print(loop)






