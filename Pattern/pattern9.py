'''Print
1  2
2  4  6
3  6  9  12
4  8  12  16  20
'''
def pat(n):
	for i in range(1,n+1):
		k=i
		for j in range(1,i+2):
			print(k*j,end='  ')
		print()
def main():
	n=int(input("Enter the number of rows"))
	pat(n)
if __name__=='__main__':
	main()