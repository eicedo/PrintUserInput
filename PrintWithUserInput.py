
s = input('Enter a random string less than 50 characters: \n')

#Print if string is alpha numeric, this will show false if there is white space 
print(s.isalnum())

#uppercase everything and verify after if it has any alphabetical characters, is alpha only checks if ALL characters are alphabetical
print(s.upper().isupper())

#check if ANY numbers in the string, converted to list to look through characters. Usedany() function
list1 = list(s)
print (any(char.isdigit() for char in list1))

#check for lower case, used list from previous step
print (any(char.islower() for char in list1))

#check for upper case, used list from previous step
print (any(char.isupper() for char in list1))












