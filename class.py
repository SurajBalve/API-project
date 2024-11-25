# def __init__  (dunder methode is  automatically call first) 
class programmer:
    company= "Extentia"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin 
             
p = programmer('suraj',10000,414102)
print(p.name,p.company,p.salary,p.pin)

class calculator:
    def __init__(self,n):
        self.n= n
        
    def squre(self):
        print(f'the square  is {self.n*self.n}')
    def cube(self):
        print(f'the cube is {self.n*self.n*self.n}')
    def squreroot(self):
        print(f'the squreroot is {self.n*1/2}')
        
a=calculator(4)
a.squre()
a.cube()
a.squreroot()
from random import randint

class Train:
    def __init__(self,trainno):
        self.trainno = trainno
    
    def book(self,fro,to):
        print(f'the ticket is booked in train no: {self.trainno} from {fro} to {to}')
    def status(self,fro,to):
        print(f'the train no {self.trainno} runnign on time from {fro} to {to}')
    def getfare(self,fro,to):
        print(f'ticket fare in trai no : {self.trainno} from {fro} to {to} is {randint(222,5555)} ')
 
 
t=Train(1038)      
t.book('pune','mumbai') 
t.status('pune','mumbai')
t.getfare('pune','mumbai')


class employee:
    name= 'suraj '
    salary = 120000 
    def __init__ (self,name,salary):
        self.name=name
        self.salary= salary
        print(f'the name is {self.name} and salary is {self.salary}')
          
p = employee('manish','100000')





