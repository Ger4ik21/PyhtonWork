class Employee: 
    new_id = 1
    def __init__(self):
            self.id = Employee.new_id
            Employee.new_id += 1
        
    def say_id(self):
          print("My id is: " +str(self.id))

class Admin(Employee):
    def say_id(self):
          super().say_id()
          print("I am admin")

class Manager(Admin):
      def say_id(self):
            super().say_id()
            print("We are responsible")


e1 = Employee()
e1.say_id()
e2 = Employee()
e2.say_id()
e3 = Admin()
e3.say_id()
e4 = Manager()
e4.say_id()

meeting = [Employee(), Admin(), Manager()]

for i in meeting:
      i.say_id()
