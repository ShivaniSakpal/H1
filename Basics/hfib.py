#WAP to print fibonnaci series before a certain range 
def fib(n):
	n1,n2=1,1
	print(n1,end=' ')
	print(n2,end=' ')
	c=n1+n2
	while c<n:
		print(c,end=' ')
		n1=n2
		n2=c
		c=n1+n2

def main():
	n=int(input("Enter range"))
	fib(n)
if __name__=='__main__':
	main()
