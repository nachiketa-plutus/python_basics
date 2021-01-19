text = input("Enter the text:\n")

if("make a lot of money" in text):
    spam = True

elif("Click this" in text):
    spam = True

elif("Subscribe" in text):
    spam = True

else:
    spam = False 

if(spam):
    print("The text has detected spam")
else:
    print("Text is spam free")
    