class twodvector:
    def __init__(self,i,j):
        self.i= i
        self.j= j
    
    def show(self):
     print(f'the vector is {self.i}i + {self.j}j')
        
class threedvector(twodvector):
    def __init__(self,i,j,k):
     super().__init__(i, j)
     self.k = k
    def show(self):
        print(f'the vector is {self.i}i + {self.j}j + {self.k}k')
    
    
# a = twodvector(2,4)
# a.show()
d= threedvector(2,4,8)
d.show()



class Animal:
    pass   
class pet():
      pass 
class Dog(pet):
    @staticmethod
    def  bark():
        print('bark')
    
a=Dog()
a.bark()