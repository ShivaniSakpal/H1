def pat(n):
	for i in range(1,n+1):
		for j in range(1,n-i+1):
			print(" ",end='')
		for _ in range(1,i+1):
			print("*",end='')
		print("")
def main():
		n=int(input("Enter number of rows"))
		pat(n)
		
if __name__=='__main__':
	main()   