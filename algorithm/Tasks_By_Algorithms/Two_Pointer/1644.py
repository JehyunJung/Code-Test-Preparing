def era_filter():
    primes=[True] * (n+1)

    primes[0]=False
    primes[1]=False

    for i in range(2,n+1):
        if primes[i]==False:
            continue
            
        times=2
        while i*times < n+1:
            primes[i*times]=False
            times+=1
    
    return [i for i in range(2,n+1) if primes[i]]
    
def solution():
    primes=era_filter()
    
    count=0
    start=0
    end=0
    length=len(primes)
    sub_sum=primes[0]

    while True:
        if sub_sum < n:
            end+=1
            if end ==length:
                break
            sub_sum+=primes[end]
        else:
            if sub_sum==n:
                print(primes[start:end+1])
                count+=1
            sub_sum-=primes[start]
            start+=1 

    print(count)        

    
    
if __name__ == "__main__":
    n=0
    with open("input1644.txt","r") as file:
        n=int(file.readline())
    solution()