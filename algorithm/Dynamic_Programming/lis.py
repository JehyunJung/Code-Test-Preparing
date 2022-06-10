from bisect import  bisect_left
def lis1():
    dp=[1] * num
    for i in range(num):
        for j in range(i):
            if datas[j] < datas[i]:
                dp[i]=max(dp[j]+1,dp[i]) 
    print(max(dp))

def lis2():
    L=[datas[0]]
    for i in range(1,num):
        if L[-1] < datas[i]:
            L.append(datas[i])
        else:
            index=bisect_left(L,datas[i])
            L[index]=datas[i]
    print(len(L))

if __name__ == "__main__":
    datas=[10,10,20,30,10,20,30,20,40]
    num=len(datas)
    lis1()
    lis2()