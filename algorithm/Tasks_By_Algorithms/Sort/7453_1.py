from collections import defaultdict
def solution():
    count=0
    ab_sum=defaultdict(int)

    for i in range(n):
        for j in range(n):
            ab_sum[A[i]+B[j]]+=1

    for i in range(n):
        for j in range(n):
            count+=ab_sum[-(C[i]+D[j])]
            if ab_sum[-(C[i]+D[j])] !=0:
                print(-(C[i]+D[j]))
    print(count)
            



if __name__ == "__main__":
    with open("input7453.txt","r") as file:
        n=int(file.readline())
        A,B,C,D=[],[],[],[]
        
        for _ in range(n):
            a,b,c,d=map(int,file.readline().split())
            A.append(a)
            B.append(b)
            C.append(c)
            D.append(d)
        
        solution()