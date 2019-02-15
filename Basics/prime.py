#WAP to accept a number from the user and check if its prime or not
def prime(n):
	flag=0
	if(n<2 or n==2):
		return 0
	elif(n%2==0):
		return 0
	else:
		for i in range(3,n//2,2):
			if(n%i==0):
				flag=1
				return 0
		if(flag==0):
			return 1
			
def main():
	n=int(input("Enter the number"))
	a=prime(n)
	if(a==0 or a==2):
		print("NOT A PRIME NUMBER")
	elif(a==1):
		print("PRIME NUMBER")
if __name__=='__main__':
	main()