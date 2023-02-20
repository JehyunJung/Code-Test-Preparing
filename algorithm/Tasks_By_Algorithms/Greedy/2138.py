from math import inf
def change_status(arr,index):
    if index >0:
        arr[index-1]=1-arr[index-1]
    arr[index]=1-arr[index]
    if index<n-1:
        arr[index+1]=1-arr[index+1]

def solution():
    for i in range(2):
        temp=before[:]
        count=0
        if i==1:
            change_status(temp,0)
            count+=1

        for index in range(1,n):
            if temp[index-1]!=after[index-1]:
                change_status(temp,index)
                count+=1

        if temp == after:
            print(count)
            
    print(-1)

if __name__ == "__main__":
    with open("input2138.txt","r") as file:
        n=int(file.readline())
        before=list(map(int,file.readline().strip()))
        after=list(map(int,file.readline().strip()))

    solution()

        
        