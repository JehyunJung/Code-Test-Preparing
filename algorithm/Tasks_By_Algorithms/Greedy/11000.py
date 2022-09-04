def solution():
    class_counts=[0] * (10**9+1)

    for start,end in classes:
        class_counts[start]+=1
        class_counts[end]-=1

    max_count=0
    for i in range(1,(10**9+1)):
        class_counts[i]+=class_counts[i-1]
        max_count=max(max_count,class_counts[i])


    return max_count

if __name__ == "__main__":
    
    N=0
    classes=[]

    with open("input11000.txt","r") as file:
        N=int(file.readline())
        classes=[list(map(int,file.readline().split())) for _ in range(N)]
    
    print(solution())