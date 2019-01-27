#WAP to accept 3 numbers and find minimum
x,y,z=eval(input("Enter 3 numbers"))
if(x<y and x<z):
			print("min",x)
elif(y<x and y<z):
			print("min",y)
else:
			print("min",z)
