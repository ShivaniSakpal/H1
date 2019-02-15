'''WAP to print the following
   *
  ***
 *****
  ***
   *
'''
def pat(n):
	for i in range(1,n+1):
		for _ in range(1,n-i+1):
			print(" ",end='')
		for _ in range(1,i*2):
			print("*",end='')
		print()
	for i in range(n-1,0,-1):
		for _ in range(n-i+1,1,-1):
			print(" ",end='')
		for _ in range(i*2,1,-1):
			print("*",end='')
		
		print()
	
def main():
	n=int(input("Enter number of rows"))
	pat(n)
if __name__=='__main__':
	main()