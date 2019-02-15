'''WAP to print the following pattern
	****
	 ***
	  **
	   *
'''
def pat(n):
	for i in range(0,n+1):
		for _ in range(1,i+1):
			print(" ",end='')
		for _ in range(1,n-i+1):
			print("*",end='')
		print()
def main():
	n=int(input("Enter the number of rows"))
	pat(n)
if __name__=='__main__':
	main()