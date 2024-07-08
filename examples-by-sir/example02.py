class Animal:
    
    def __init__(self, age):
        self.name = None
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def __str__(self):
        msg = f"Animal(name: '{self.name}' , age: {self.age})"
        return msg

# End of class defintion

a = Animal(3)
a.set_name("Jimmy")
print(f"Animal name: {a.get_name()}, age: {a.get_age()}")
a.set_age(4)
print(f"Updated Info: {a}")