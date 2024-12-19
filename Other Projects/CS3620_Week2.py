#Part 1
bodyWeight = int(input("Enter Body Weight in kg: "))
Height = float(input("Enter Height in Meters: "))

BMI = bodyWeight/(Height**2)
print("your BMI", round(BMI, 2))

#part 2
def divBy0(number1, number2):
    try:
        print(number1/number2)
    except ZeroDivisionError:
        print("can't divide by zero")

#part 3
file = open("demo.txt", 'w')
file.write("Here is some datat")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()

file = open("demo.txt", "a")
file.write("HEREISAPPPEND")
file.close()

#part 4
prices = {'mouses':10, 'keyboard':20,'monitor':100,'computer':90000,'bitcoin':111111}

def getPrice(productName):
    return prices.get(productName)

print(getPrice("keyboard"))

#part 5
mylist = []
for i in range(1,101,2):
    if(i % 2 != 0):
        mylist.append(i)
print(mylist)