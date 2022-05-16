
#gives the result of sum of how many opportunities to get n
def num_sums(n,w):
    if n==0:
        return 1
    if n<0:
        return 0
    if n>0:
        return sum([num_sums(n-i,w)for i in w])
    
#if the user putted a number that is different from 0 the def takes his first number as n and the rest of the numbers are list
x=1
while x!='0':
    x=input('')
    if x=='0':
        break
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    z1=x[0]
    z2=x[1:]
    a1=num_sums(z1,z2)
    print(a1)
        