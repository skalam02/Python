#Stylianos Kalamaras
#05/20/17
#CSCI360 Final

#This program generates a k bit RSA modulus where 32<=k<=64.

import math
import random
import secrets


# Euclid's Algorithm. Returns the GCD of a and b.
def GCD(a, b):
  while b:
    (a, b) = (b, a % b)
  return a

# Primality checking using the Sieve of Erastosthenes.
def IsPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def generateRSAPrime(k=1):

    while (k<32 or k>64):
        k=int(input("Value must be between 32-64 bits, re-enter value"))

    i=100*k
    r1 = secrets.choice(range(2**(k-1),2**k-1))

    while i>0:
        if (r1 % 3 != 1 and r1 % 5 != 1 and IsPrime(r1)):
            return r1
        r1 = secrets.choice(range(2**(k-1),2**k-1))
        i-=1

    print("no value generated")


# Euclid's Extended Algorithm. Returns d, the gcd of
# a and b, as well as ud and vd, where
#        d = ud * a + vd * b
def EuclidExtended(a, b):
    c, d = a, b
    uc, vc, ud, vd = 1, 0, 0, 1

    while c:
        q = d // c
        c, d = (d - q * c), c
        uc, vc, ud, vd = (ud - q * uc), (vd - q * vc), uc, vc

    return d, ud, vd

def generateRSAKey(k):

    while (k<64 or k>128):
        k = int(input("Key must be in range 64-128 bits, re-enter value: "))

    p= generateRSAPrime(k//2)
    q = generateRSAPrime(k//2)
    n = p*q
    t = (((p-1)*(q-1))//GCD(p-1,q-1))

    g,u,v = EuclidExtended(3,t)

    if (g!=1):
        print("Error, GCD is not 1")
        return

    d3 = u % t

    g,u,v = EuclidExtended(5,t)

    if (g!=1):
        print("Error, GCD is not 1")
        return

    d5 = u%t

    return p,q,n,d3,d5

def main():
    k = int(input("RSA Modulus Bit Size: "))
    p,q,n,d3,d5 = generateRSAKey(k)
    print("p = ",p)
    print("q = ",q)
    print("n = ",n)
    print("d3 = ",d3)
    print("d5 = ",d5)

main()