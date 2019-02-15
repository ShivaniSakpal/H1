#WAP to accept 2 strings in rotation of first 
x=str(input("Enter a string"))
s=str(input("Enter the string to be checked"))
if len(x)==len(s):
	print(s in x+x)
else:
	print("False")
		
