import string
import random 
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
# Taking password length from user 
plen = int(input("Enter Password Length : "))
# Shuffling password using library
ran=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=plen))
print("The randomly generated string is : " + str(ran))

