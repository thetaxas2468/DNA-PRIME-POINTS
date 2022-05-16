
import random
import timeit
#def even that gives even and odd from n and returns get even odd parts function that has the numbers
def even(n):
    if n%2==1:
        return 0
    if n%2==0:
        return 1+(even(n//2))
def odd(n):
    if n%2==1:
        return n
    if n%2==0:
        return odd(n//2)
def get_even_odd_parts(n):
    k1=even(n)
    k2=odd(n)
    return [k1,k2]
     

def modular_power(a,b,n):
    """ computes a**b (mod n) using iterated squaring
    assumes b is a nonnegative integer """
    result = 1
    while b>0: # b has some bits left
        if b%2 == 1: # b is odd
            result = (result*a)%n
        a = (a*a)%n
        b = b//2
    return result
#return if the number is suspected =prime or not and if it has a big advantage of being prime
def is_suspected_prime(n,t,s):
    a=random.randint(0,n-1)    
    d=modular_power(a,t,n)
    if d==1 or d==n-1:
        return True
    for i in range(1,s):
        d=modular_power(d,2,n)
        if d==n-1:
            return True
    return False
# reutrn if the number we have is true prime or false not prime(not 100%) cause it return if it is probably prime not for sure.
def probably_prime(n,num_iterations):
    s=even(n-1)
    t=odd(n-1)
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return False
    for i in range(num_iterations):
        if is_suspected_prime(n,t,s)==False:
            return False
    return True
# it generate a big numbers and all are primes and it runs 10 times(num iterations)
def generate_prime(num_bits,num_iterations):
    x=0
    while x==0:
        q1=random.getrandbits(num_bits)
        q2=probably_prime(q1,num_iterations)
        if q1%2==0:
            q1=q1+1
            if q2==False:
                if q2==True:
                    return q1
        if q1%2==1:
            if q2==True:
                return q1
# def main that do every thing i need for better quality
def main():
    f5=''
    t1=timeit.default_timer()
    for i in range(10):
        x32=generate_prime(1024,10)
        f5+=str(x32)
        f5+='\n'
    t2=timeit.default_timer()
    print(t2-t1)
    f2=open('primes.txt','w')
    f2.write(f5)
    f2.close()   
main()
    

  
    
            

   