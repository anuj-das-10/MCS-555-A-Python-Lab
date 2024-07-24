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


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self): return f"000{self.rid}"
    def get_parent1(self): return self.parent1
    def get_parent2(self): return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        is_parent1_same = self.parent1.rid == other.parent1.rid
        is_parent2_same = self.parent2.rid == other.parent2.rid 

        is_parent1_opposite = self.parent1.rid == other.parent2.rid
        is_parent2_opposite = self.parent2.rid == other.parent1.rid
        return (is_parent1_same and is_parent2_same) or (is_parent1_opposite and is_parent2_opposite)

    def __str__(self): return f"Rabbit: {self.get_rid()}"


# End of class defintion



# Example of class Animal
a = Animal(3)
a.set_name("Jimmy")
print(f"Animal name: {a.get_name()}, age: {a.get_age()}")
a.set_age(4)
print(f"Updated Info: {a}")


# Example for class Rabbit
r1 = Rabbit(4)
r2 = Rabbit(4)
r3 = Rabbit(4)
print("r1 = ", r1)
print("r2 = ", r2)
print("r3 = ", r3)

print("\nAdding two Rabbits")
r4 = r1 + r2
print("r4 = ", r4)
print(f"Parent-1 of r4 = {r4.get_parent1()}")
print(f"Parent-2 of r4 = {r4.get_parent2()}")


print("\nEquality test of Rabbit:")
r5 = r3 + r4
print(f"Parent-1 of r5 = {r5.get_parent1()}")
print(f"Parent-2 of r5 = {r5.get_parent2()}")

r6 = r4 + r3
print(f"Parent-1 of r6 = {r6.get_parent1()}")
print(f"Parent-2 of r6 = {r6.get_parent2()}")

print("r5 == r6 ? ",r5 == r6)
