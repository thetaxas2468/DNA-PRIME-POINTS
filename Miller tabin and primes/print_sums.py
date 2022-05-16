
#def that gives all the opportunities to coutn a number from a given list
def print_sum(x,y):
    w=[]
    for i in y:
        if (x-i>0):
            w1=print_sum(x-i,y)
            for j in w1:
                w.append(str(i)+' + '+j)
        if (x-i==0):
            w.append(str(i))
    return w
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
    a1=print_sum(z1,z2)
    for i in a1:
        print(i)

       