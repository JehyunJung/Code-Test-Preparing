from math import factorial
def solution():
    """ di=[[0]* (k+1) for _ in range(n+1)] 
    di[0][0]=1

    for i in range(k+1):
        di[0][i]=1   

    for i in range(1,n+1):
        for j in range(1,k+1):
            di[i][j]=di[i-1][j]+di[i][j-1]
    
    print(di[n][k]%1000000000) """
    count=factorial(n+k-1)//(factorial(k-1)*factorial(n))
    print(count%1000000000)
if __name__ == "__main__":
    n,k=0,0
    with open("input2225.txt","r") as file:
        n,k=map(int,file.readline().split())
    solution()  