def solution():
    di=[1] * num

    for i in range(num):
        for j in range(i):
            if datas[j] < datas[i]:
                di[i]=max(di[i],di[j]+1)
    
    
    print(max(di))
if __name__ == "__main__":
    num=0
    datas=[]

    with open("input1965.txt","r") as file:
        num=int(file.readline())
        datas=list(map(int,file.readline().split()))
    
    solution()