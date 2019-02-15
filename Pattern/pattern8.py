'''Print
4321*
321**
21***
1****

'''
def pat(n):
	for i in range(1,n+1):
		for j in range(n-i+1,0,-1):
			print(j,end='')
		for _ in range(0,i):
			print("*",end='')
		print()
def main():
	n=int(input("Enter the number of rows"))
	pat(n)
if __name__=='__main__':
	main()