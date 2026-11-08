name = input("Enter the full name: ")

# result = name.find("i")
# result = len(name)
# result = name.isupper()
# result = name.islower()
# result = name.upper()
# result = name.lower()
result = name.rfind("a")
result = name.capitalize()
result = name.replace("a", "p")
result = name.isalpha() # is alpha methods check a string contains only alphabetical character either space nor special characters. if contain it will show false in the terminal.
result = name.isdigit() # is digit methods check that if string contains characters or alphabets it will show False and for true must all numbers
result = name.count("4")
result = name.find(" ")
print(result)
