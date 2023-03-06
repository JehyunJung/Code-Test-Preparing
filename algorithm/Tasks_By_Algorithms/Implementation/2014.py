from heapq import heappush,heappop,heapify
def solution():
    last_result=0
    heap=primes[:]
    heapify(heap)

    for _ in range(n):
        last_result=heappop(heap)
        
        for prime in primes:
            heappush(heap,last_result*prime)

            if last_result % prime==0:
                break

    print(last_result)


if __name__ == "__main__":
    with open("input2014.txt","r") as file:
        k,n=map(int,file.readline().split())
        primes=list(map(int,file.readline().split()))

    solution()