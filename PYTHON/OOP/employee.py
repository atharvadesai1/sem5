class Employee:
    emp_list = {}
    manager = {}
    def __init__(self,fname,lname,emp_id,type):
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.type = type
        self.emp_list[self.emp_id] = self

    def info(self,obj):
        return (obj.fname,obj.lname,obj.emp_id,obj.type)
    
class Manager(Employee):
    developer = {}
    tester = {}
    def __init__(self, fname, lname, emp_id):
        Employee.__init__(self,fname,lname,emp_id,'Manager')
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.type = 'Manager'
        super().manager[self.emp_id] = self
        
    def add(self,obj):
        if(obj.type=='Developer'):
            self.developer[obj.emp_id] = obj
        if(obj.type=='Tester'):
            self.tester[obj.emp_id] = obj

    def remove(self,obj):
        if(obj.type=='Developer'):
            del self.developer[obj.emp_id]
        if(obj.type=='Tester'):
            del self.tester[obj.emp_id]

    def display(self):
        print('List of Employess:')
        for i in super().emp_list:
            print(str(i) + " "+ str(super().info(super().emp_list[i])))
        print()
        print('List of Managers:')
        for i in super().manager:
            print(str(i) + " "+ str(super().info(super().manager[i])))
        print('List of Developers:')
        for i in self.developer:
            print(str(i) + " "+ str(super().info(self.developer[i])))
        print()
        print('List of Testers:')
        for i in self.tester:
            print(str(i) + " "+ str(super().info(self.tester[i])))

class Developer(Employee):
    def __init__(self, fname, lname, emp_id):
        Employee.__init__(self, fname, lname, emp_id, 'Developer')
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.type = 'Developer'

class Tester(Employee):
    def __init__(self, fname, lname, emp_id):
        Employee.__init__(self, fname, lname, emp_id, 'Tester')
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.type = 'Tester'

atharva = Manager('Atharva','Desai',1.0)
sanjay = Developer('Sanjay','Rathod',1.1)
atharva.add(sanjay)
raghav = Tester('Raghav','Patel',1.2)
atharva.add(raghav)
atharva.display()
