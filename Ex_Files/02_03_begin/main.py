NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] #[:2] will print the first 2 elements
GEORGE_RINGO = NAMES[2:] #[2:] will print all elements after the second one, not including the second one
REVERSE = NAMES[::-1] #start, stop, step
  #[::-1] start regularly, we dont have a stop, and step by -1, so start from the back
EVERY_OTHER = NAMES[::2]
  #[::2] step by 2, print every other name starting with the first one (start is empty, therefore start regularly)

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)
