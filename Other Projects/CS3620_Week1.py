p = int(input("What is the principle: "))
n = int(input("What is the number of years: "))
r = int(input("What is the rate of intrest: "))

simpleIntrest = ((p*n*r)/100)
print(simpleIntrest)

favFood = ["Pizza", "Watermelon", "Mac & Cheeze", "Ramen", "Rice"]
print(favFood[2])
favFood.append("Water")
favFood.append("Pizza Again")
print(favFood)
favFood[2] = "tacos"
print(favFood)

for i in range(0,5):
    print("I am a programmer")

for i in range(1,10):
    print(i**2)