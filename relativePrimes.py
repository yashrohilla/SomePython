#!/bin/env/python3
import math

def isPrime(n):
    for a in range(3,100):
        if relativePrime(a,n) == True:
            if a**(n-1)%n != 1:
                return False
    return True




def relativePrime(a,b):
    factorsA = []
    factorsB = []
    for i in range(1, a+1):
        if a%i == 0:
            factorsA.append(i)
    for i in range(1, b+1):
        if b%i == 0:
            factorsB.append(i)
    listFactor = list(set(factorsA).intersection(factorsB))
    #print(listFactor)
    if listFactor[0] == 1 and len(listFactor) == 1:
        return True

def totient(n):
    count = 0
    for i in range(1,n):
        factorA, factorB = relativePrime(i,n)
        listFactor = list(set(factorA).intersection(factorB))
        if listFactor[0] == 1 and len(listFactor) == 1:
            count += 1
    return count


if __name__ == "__main__":
    #n = input('Enter number to get totient: ')
    #print totient(n)
    #for i in range(1, 8):
    #    relativePrime(i, 7)

    #print(relativePrime(23,14))
    #print(isPrime(4547337172376300111955330758342147474062293202868155909489))
    print([x for x in range(901, 1000) if isPrime(x)])
