greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}" #string interpolation using opening and closing curly brackets

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper()) #prints all upper case
print(formatted.lower()) #prints all lower case
print(formatted.replace("John", "Paul")) 
  #prints in the same format as it initially did, except replaces "John" with "Paul"
