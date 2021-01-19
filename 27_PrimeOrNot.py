num = int(input("Please enter the number you wish to test for being prime or not: "))

for i in range(2, num):
    if(num%i == 0 and num!=2):
       print("The number entered is not prime")
       break
else:
   print("Prime Number")
        