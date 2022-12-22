#while test again
print("Welcome to the sample test of my second(?) repo git test")

name = str(input("Please enter your name: "))
num = int(input("Please enter desired looping sequences total: "))
i = 0
storage = list()

while num > i:
    pos = int(input("enter pos: "))
    storage.append(pos)
    print(storage)
    i += 1

print()
print()
print("Thank you for visiting this test!, the result below showed up that this test is working!")
print(storage)