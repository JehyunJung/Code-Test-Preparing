def solution():
    start,end=0,0
    checked=[False]*100001
    count=0

    while end < n:
        if not checked[numbers[end]]:
            checked[numbers[end]]=True
            end+=1
            count+=(end-start)
        else:
            while checked[numbers[end]]:
                checked[numbers[start]]=False
                start+=1
    print(count)


if __name__ == "__main__":
    with open("input13144.txt", "r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    solution()