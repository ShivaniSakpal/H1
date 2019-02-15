'''WAP to accept a number and check if its palindrome or not
'''
def palindrome(a):
	temp=0
	rem=0
	n=a
	while n>0:
		rem=n%10
		temp=temp*10+rem
		n=n//10
	return temp

def main():
	a=int(input("Enter a Number:"))
	rev=palindrome(a)
	if (rev==a):
		print("Palindrome")
	else:
		print("Not Palindrome")
	
	
if __name__=='__main__':
	main()