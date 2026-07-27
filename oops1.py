class Employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"



    def travel(self, destination):
        print(f"Travelling to {destination}")





# create an obj/instance of the class
sam = Employee()
sam.name = "Sam" # attribute outside the class

print(sam.salary)
print(sam.name)
sam.travel("Bangalore")