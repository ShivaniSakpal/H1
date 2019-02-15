def pat(n):
	for i in range(1,n+1):
		k=i
		for j in range(1,i+2):
			print(k,end='  ')
			k*=2
		print()
def main():
	n=int(input("Enter the nuber of rows"))
	pat(n)
if __name__=='__main__': 
	main()