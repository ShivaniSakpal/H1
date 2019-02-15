def pat(n):
	for i in range(n+1):
		for j in range(i):
			print("*",end='')
		print()
def main():
		n=int(input("Enter number of rows"))
		pat(n)
		
if __name__=='__main__':
	main()  