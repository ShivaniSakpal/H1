#WAP to accept a number from the user and print in simple word eg:273 OUTPUT: two seven three
def rev(n):
	rem=0
	while n>0:
		dig=n%10
		rem=rem*10+dig
		n=n//10
	return(rem)	
def check(n1):
	rem=0
	while n1>0:
		dig=n1%10
		rem=rem*10+dig
		n1=n1//10
		if dig==0:
			print("Zero",end=' ')
		elif dig==1:
			print("One",end=' ')
		elif dig==2:
			print("Two",end=' ')
		elif dig==3:
			print("Three",end=' ')
		elif dig==4:
			print("Four",end=' ')
		elif dig==5:
			print("Five",end=' ')
		elif dig==6:
			print("Six",end=' ')
		elif dig==7:
			print("Seven",end=' ')
		elif dig==8:
			print("Eight",end=' ')
		elif dig==9:
			print("Nine",end=' ')
			
			
			
def main():
	n=int(input("Enter the number"))
	n1=rev(n)
	check(n1)
if __name__=='__main__':
	main()