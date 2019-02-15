#WAP to accept 2 strings  from the user and swap their first two character
s1=str(input("Enter the string"))
s2=str(input("Enter 2nd string"))
st1=s1[:2]
st2=s2[:2]
s1=st2+s1[2:]
s2=st1+s2[2:]
print (s1)
print (s2)
