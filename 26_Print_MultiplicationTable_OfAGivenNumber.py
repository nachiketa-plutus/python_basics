Num = int(input("Please enter the number you wish to see the table of: "))
Num2 = int(input("Please enter the second number: "))

for i in range(1,11):
    print(f"{Num}x{i}")
    #Using Fstrings

for j in range(1,11):
    print(str(Num2) + "x" + str(i) + "=" + str(Num2*i))
    #Using concatenation of strings 
    
    # Multi[i]=i*Num
    # print(Multi[i])
    # i=i+1
    # if i==10:
    #     break
    