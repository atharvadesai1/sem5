class Animal:
    def  __init__(self,name,color,legs,type):
        self.name = name
        self.color = color
        self.legs = legs
        self.type = type

    def printproperties(self):
        print(f"{self.name} is my {self.type}.\nIt has {self.legs} legs and is {self.color} in color.")

goofy = Animal("Goofy","white",4,"dog")
scoop = Animal("Scoop","brown",2,"monkey")
trevon = Animal("Trevon","black",4,"")
goofy.printproperties()