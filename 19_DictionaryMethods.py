myDict = { 
    "Python": "A Language",
    "Nachiketa": "Self-proclaimed loner",
    "Marks": [23, 25, 42],
    5: 5,
    "AnotherDict": {" Nachi": "Nunga", "Nunga": "Nachi"}
}

# Dictionary Methods

print(myDict)
print(myDict.items()) # prints the (key, value) pair for all the comtents of the dictionary
print(list(myDict.keys())) # prints the keys of the dictionary in a list form
print(myDict.values()) # prints the values of the dictionary
updateDict = {
    "Kuldeep": "Friend",
    "Rahul": "Friend 2",
    "Priyank": "Friend 3",
    "Nachiketa": "Loner"
}
myDict.update(updateDict)
print(myDict)
print(myDict["Nachiketa"])
print(myDict.get("Priyank"))



