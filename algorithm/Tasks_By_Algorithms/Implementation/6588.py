import sys
def era_filter():
    check=[False]*(max_number+1)
    primes=[]

    for i in range(2,max_number+1):
        if check[i]:
            continue
        primes.append(i)
        for j in range(i,max_number+1,i):
            check[j]=True

    return primes

def solution():
    primes=era_filter()[1:]
    prime_set=set(primes)
    for query in queries:
        for prime in primes:
            if (query-prime) in prime_set:
                print(f"{query} = {prime} + {(query-prime)}")
                break
        else:
            print("Goldbach's conjecture is wrong.")

if __name__ == "__main__":
    queries=[]
    max_number=1000000
    with open("input6588.txt","r") as file:
        while True:
            temp=int(file.readline())
            if temp == 0:
                break
            queries.append(temp)    
    solution()