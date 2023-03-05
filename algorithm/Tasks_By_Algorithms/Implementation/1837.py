from math import sqrt

def perform_division(divisor):

    remainder=secret[0]
    quantifier=0
    
    for index in range(1,length_of_secret+1):
        quantifier=quantifier * 10 + remainder//divisor

        if index < length_of_secret:
            remainder= remainder%divisor * 10 + secret[index]
        else:
            remainder= remainder%divisor

    return remainder,quantifier

def era_filter(k):
    checked=[False]*(k+1)
    primes=[]
    for number in range(2,k+1):
        if checked[number]:
            continue
        primes.append(number)
        times=1

        while number * times <= k:
            checked[number*times]=True
            times+=1
        
        

    return primes

def solution():
    primes=era_filter(k)
    for prime in primes:
        remainder,quantifier=perform_division(prime)
        if remainder==0:
            print(f"BAD {min(quantifier,prime)}")
            break
    else:
        print("GOOD")

    print(era_filter(101))


if __name__ == "__main__":
    with open("input1837.txt","r") as file:
        secret,k=map(str,file.readline().split())
        secret=list(map(int,secret))
        k=int(k)
    length_of_secret=len(secret)
    solution()