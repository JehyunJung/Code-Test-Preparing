from copy import deepcopy
def solution():
    di=deepcopy(arr)
    
    if n>=2:
        di[0][1]+=di[1][0]
        di[1][1]+=di[0][0]

    if n>=3:
        for col in range(2,n):
            di[0][col]+=max(di[1][col-1],di[1][col-2])
            di[1][col]+=max(di[0][col-1],di[0][col-2])
    
    return max(di[0][-1],di[1][-1])
                
    
if __name__ == "__main__":
    n=0
    arr=[]

    with open("input9465.txt","r") as file:
        n=int(file.readline())
        arr=[list(map(int,file.readline().split())) for _ in range(2)]
    
    print(solution())