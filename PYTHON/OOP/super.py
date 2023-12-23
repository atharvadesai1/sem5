class Parent:
    def __init__(self,fname,fage) -> None:
        self.fname = fname
        self.fage = fage

    def printin(self):
        print("Baap hu tera")

class Child(Parent):
    def __init__(self, fname, fage,name,age):
        super().__init__(fname, fage)
        self.name = name
        self.age = age

    def information(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My father's name is {self.fname}")
        print(f"My father's age is {self.fage}")

ramesh = Child('Suresh',50,'Ramesh',20)
print(ramesh)
ramesh.information()
ramesh.printin()

ramcharan = Parent('Ramcharan',62)
print(ramcharan)
ramcharan.printin()
        