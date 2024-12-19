#Part 1
def studentDiscount(number):
    return number*.9

def addDiscount(number):
        return number*.95

print(addDiscount(studentDiscount(100)))

#Part 2
print((lambda x: x*(x+5)**2)(5))

#Part 3
prices = [10,20,30,40,50,60,70,80,90,101]
discountPrices = list(map(lambda x:studentDiscount(x), prices))
print(discountPrices)

#part 4
class Computer:
    def __init__(self, weight ):
         self.weight  = weight 

    def getSpecs(self):
        self.weight  = input("what is the weight: ")

    def displaySpecs(self):
        print(self.weight )


class Desktop(Computer):  
    def __init__(self, weight):
        self.width  = "" 

    def getSecialSpecs(self):
        self.width  = input("what is the width: ")

    def displaySpecialSpecs(self):
        print(self.width)


class Laptop(Computer):
    def __init__(self, weight):
        self.length  = "" 

    def getSecialSpecs(self):
        self.length  = input("what is the length: ")

    def displaySpecialSpecs(self):
        print(self.length)


bradonLaptop = Laptop("")
bradonLaptop.getSpecs()
bradonLaptop.displaySpecs()
bradonLaptop.getSecialSpecs()
bradonLaptop.displaySpecialSpecs()

bradonDesktop = Desktop("")
bradonDesktop.getSpecs()
bradonDesktop.displaySpecs()
bradonDesktop.getSecialSpecs()
bradonDesktop.displaySpecialSpecs()

#part 5
class overloading:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return(self.x + other.x)
    
over1 = overloading(5)
over2 = overloading(5)
print(over1 * over2)



