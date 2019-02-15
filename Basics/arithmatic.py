'''WAP to accept 2 numbers and perform  
1. Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exponentional
'''
n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
print("Add : ",n1+n2)
print("Subtract : ",n1-n2)
print("Multiply : ",n1*n2)
print("Division : ",n1/n2)
print("Exponention : ",n1 ** n2)
power=1
i=1
while(i<=n2):
	power=power*n1
	i=i+1
print("Result Power =   ",power)
