sub1 = int(input("Please enter the marks for subject 1:\n"))
sub2 = int(input("Please enter the marks for subject 2:\n"))
sub3 = int(input("Please enter the marks for subject 3:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You have failed")

elif((sub1+sub2+sub3)/3<40):
    print("Failed")

else:
    print("Passed the test")
