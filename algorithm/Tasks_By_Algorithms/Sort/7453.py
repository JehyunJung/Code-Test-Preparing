from bisect import bisect_left,bisect_right
def count_range(arr,num):
    left=bisect_left(arr,num)
    right=bisect_right(arr,num)

    return right-left
    
def solution():
    count=0
    ab_sum=[]
    cd_sum=[]

    for i in range(n):
        for j in range(n):
            ab_sum.append(A[i]+B[j])
            cd_sum.append(C[i]+D[j])
    
    ab_sum.sort()
    cd_sum.sort()
    i,j=0,n**2-1
    while i < n**2 and j >=0:

        if ab_sum[i]+cd_sum[j]==0:
            i+=1
            j-=1
            
            left_count,right_count=1,1
            while i<n**2 and ab_sum[i] == ab_sum[i-1]:
                i+=1
                left_count+=1
            
            while j>=0 and cd_sum[j] == cd_sum[j+1]:
                j-=1
                right_count+=1
            
            count+=(left_count*right_count)

        elif ab_sum[i] + cd_sum[j] <0:
            i+=1
        else:
            j-=1

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