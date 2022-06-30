from collections import defaultdict
def solution():
    accum_A=defaultdict(int)
    count=0

    for i in range(numA):
        temp=A[i]
        accum_A[temp]+=1
        for j in range(i+1,numA):
            temp+=A[j]
            accum_A[temp]+=1

    for i in range(numB):
        temp=B[i]
        count+=(accum_A[sub_sum-temp])
        for j in range(i+1,numB):
            temp+=B[j]
            count+=(accum_A[sub_sum-temp])

    print(count)

if __name__ == "__main__":
    sub_sum=0
    numA,numB=0,0,
    A=[]
    B=[]

    with open("input2143.txt","r") as file:
        sub_sum=int(file.readline())

        numA=int(file.readline())
        A=list(map(int,file.readline().split()))

        numB=int(file.readline())
        B=list(map(int,file.readline().split()))
        
    solution()