# Same output for single quoted and double quoted strings. 
# Output includes string portion enclosed in single quotes.

List = [44, 55, 44.55, True, "Raju", False, "Rahim", 33]
print(List)
List2 = [44, 55, 44.55, True, 'Raju', False, 'Rahim', 33]
print(List2)

# List Slicing 

List3 = ["Afzal", "Manish", 33.46, True, False, 78]
print(List3)    
print(List3[0:3])
print(List3[0:])
print(List3[:-1])
print(List3[-3:-1])
print(List3[:4])