'''WAP to print
   A
  BAB
 CBABC
DCBABCD
'''
def pat(n):
	for i in range(1,n+1):
	
		x=i
		for _ in range(1,n-i+1):
			print(" ",end='')
		for j in range(1,i*2):
			print(chr(x+64),end='')
			if j<i:
				x=x-1
			else:
				x=x+1
		print()
def main():
	n=int(input("ENTER ROWS"))
	pat(n)
if __name__=='__main__':
	main()