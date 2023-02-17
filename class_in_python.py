
class Employee():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + " " + lname
    
    def favourite_quote(self,quote):
        return f"{self.fname}'s favourite quote is {quote}"

# admin = Employee("David","Akuma")
# finance = Employee("Shola","Ogb")

# print(admin.fname)
# print(finance.fullname)

#create a class for students of GenUni
#should have attributes for first and last name of students
# the third attribute should be for email, which is concatenating
#first name, last name and @genuni.co.uk
#print out students first name, last name and email
# firstname.lastname@GenUni.co.uk

# class Students():
#     def __init__(self,first_name,last_name,):
#         self.full_name = first_name
#         self.last_name = last_name
#         self.fullname = first_name + " " + last_name
#         self.email = first_name + "." + last_name + "@GenUni.co.uk"

# student1 = Students("Jak","Bowes")
# student2 = Students("David","Akuma")

# print(student1.email)

#create a method that generates the student id
# by concatenating the students first and last names
# with their birth months as a parameter when you call the
# method DAVIDAKUMA06