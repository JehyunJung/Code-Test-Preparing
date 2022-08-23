from math import perm,comb,factorial
def print_list(lists):
    print("DI")
    for list in lists:
        print(list)
def solution():
    di=[[0] * num for _ in range(num)]
    
    

    if num==1:
        return 1
    di[1][1]=1

    for i in range(2,num):
        di[i][1]=factorial(i-1)
        for j in range(2,i):
            temp=0
            for k in range(i-1,j-2,-1):
                temp+=di[k][j-1]*perm(i-1,i-1-k)

            di[i][j]=temp
        di[i][i]=1

    print_list(di)
    #실제 구하는 과정
    count=0
    if L==1:
        count=di[num-1][R-1]
    elif R==1:
        count=di[num-1][L-1]
    
    else:
        for i in range(num-2,L-2,-1):
            count+=(comb(num-1,i)*di[i][L-1]*di[num-i-1][R-1])

    return count    

if __name__ == "__main__":
    num,L,R=6,3,2
    """ 
    with open("input1328.txt","r") as file:
        num,L,R=map(int,file.readline().split())  
        """

    print(solution())