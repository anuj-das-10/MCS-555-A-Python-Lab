class Inset:
    
    def __init__(self):
        self.values = []

    def insert(self, x):
        if x not in self.values:
            self.values.append(x)

    def remove(self, x):
        try:
            self.values.remove(x)
        except:
            raise ValueError(f"{x} not found in the list.") 

    def member(self, x):
        return x in self.values

    def get_member(self):
        return self.values


    def __str__(self):
        self.values.sort()
        result = ""
        for num in self.values:
            result += (str(num) + ", ")

        msg = "{" + result[:-2] + "}"
        return msg

# End of class definition


ob = Inset()
ob.insert(3)
ob.insert(4)
ob.insert(1)

x = 2
print(f"Is {x} member of Inset?  {ob.member(x)}")
print(f"All the members of Inset: {ob.get_member()}")

print(ob)
    