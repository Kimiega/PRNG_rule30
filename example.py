import randgenk30 as rand
print("5 random numbers from 0 to 1000 inclusive")
for i in range(5):
    print(rand.nextRandom(1000))
print("5 random numbers from 10 to 20 inclusive")
for i in range(5):
    print(rand.nextRandom(10, 20))
print("5 random numbers")
for i in range(5):
    print(rand.nextRandom())
