NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i]) #print name and age on the index i
    i += 1 #increment i

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES): #zip, zips the two together
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name) #reverse names

for i in range(5):
    print(i)

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i}{name}") #comes in handy when you want to know where you are at
