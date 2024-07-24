# Example of Inheritance

import datetime as dt

class Person:
    def __init__(self, name):
        self.name = name
        self.birthday = None

        try:
            last_blank = name.rindex(' ')
            self.last_name = self.name[last_blank+1:]
        except:
            self.last_name = name

    def __str__(self): return self.name

    def get_name(self): return self.name
        
    def get_last_name(self): return self.last_name

    def set_birthday(self, birthdate): self.birthday = birthdate


    def get_age(self):
        if self.birthday == None:
            return f"{self.name}, please update your birth date!"
        else:
            return (dt.date.today() - self.birthday).days // 365
    

    def __lt__(self, other):
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name



class MIT_Person(Person):
    _next_uid_number = 0
    
    def __init__(self, name):
        super().__init__(name)
        self.uid_num = MIT_Person._next_uid_number
        MIT_Person._next_uid_number += 1

    def get_uid(self): return self.uid_num

    def __lt__(self, other): return self.uid_num < other.uid_num



# Objects of Person Class
p1 = Person('Jin Khazama')
print(p1)
print(p1.get_name())
print(p1.get_last_name())
print(p1.get_age())
p1.set_birthday(dt.date(2000, 9, 10))
print(p1, "is", p1.get_age(), "years old!")

p2 = Person('Nina William')
p3 = Person("Nina Johnson")
print(p1, "<", p2, " is ", p1 < p2)
print(p2, "<", p3, " is ", p2 < p3)


print("\n")

# Objects of MIT_Person class
m1 = MIT_Person('Mark Guttag')
m2 = MIT_Person('Billy Bob Beaver')
m3 = MIT_Person('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')
print('m1 < m2 =', m1 < m2)
print('m3 < m2 =', m3 < m2)
print('p4 < m1 =', p4 < m1)

print(f"UID: {m1.uid_num} & Name: {str(m1)}")
print(f"UID: {m2.uid_num} & Name: {str(m2)}")
print(f"UID: {m3.uid_num} & Name: {str(m3)}")

# Attribute Error: 'Person' object has no attribute 'uid_num'
# print(f"UID: {p4.uid_num} & Name: {str(p4)}")           