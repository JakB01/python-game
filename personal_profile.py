
from addition import add
from subtraction import sub
from division import div
from multiply import mult

# add_number = add(9,6)
# sub_number = sub(4,2)
# div_number = div(6,3)
# mult_number = mult(4,3)

# print(mult_number)

def new_function(a, b):
    add_new = add(a,b)
    sub_new = sub(a,b)
    div_new = div(a,b)
    mult_new = mult(a,b)
    return add_new, sub_new, div_new, mult_new
var1 = new_function(10,5)
print(var1)



