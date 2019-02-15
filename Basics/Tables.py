#WAP to accept an integer and print tables from it till 2 to n
n=int(input("Enter a number"))
for j in range(2,n+1):
	print("Table of",j)
	for i in range(11):
		
		print(j,'X',i,'=',(n*i))
		
