Letter = '''\nDear <|NAME>, It is with great pleasure
that I am informing you of your selection for the aforementioned
position

<|DATE>'''

name  = input("Please enter your name for the record:\n")
date = input("Please state today's date for the record:\n")
Letter = Letter.replace("<|NAME>", name)
Letter = Letter.replace("<|DATE>", date)
print(Letter)       

