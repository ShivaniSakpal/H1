def add(x,y):
	return(x+y+10)
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def main():
	print("MENU")
	print("1.ADDITION")
	print("2.SUBTRACTION")
	print("3.MULTIPLICATION")
	print("4.DIVISION")
	n=int(input("Enter your choice"))
	if(n==1):
		x,y=eval(input("Enter 2 numbers"))
		a=add(x,y)
		print("ADDITION:",a)
	elif(n==2):
		x,y=eval(input("Enter 2 numbers"))
		s=sub(x,y)
		print("SUBTRACTION:",s)
	elif(n==3):
		x,y=eval(input("Enter 2 numbers"))
		m=mul(x,y)
		print("MULTIPLICATION:",m)
	elif(n==4):
		x,y=eval(input("Enter 2 numbers"))
		d=div(x,y)
		print("DIVISION:",d)
	else:
		print("WRONG CHOICE")
if __name__=='__main__':
	main()
