#WAP to accept a string from the user , replace all the occurences of first character with * in the remaining part of the string
s=str(input("Enter a string"))
x=s[0]+s[1:].replace(s[0],'*')
print (x)