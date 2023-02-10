def solution():
    rankings=[1] * n
    for i in range(n):
        for j in range(n):
            if peoples[i][0]<peoples[j][0] and peoples[i][1]<peoples[j][1]:
                rankings[i]+=1
    
    print(*rankings)
if __name__ == "__main__":
    with open("input7568.txt","r") as file:
        n=int(file.readline())
        peoples=[list(map(int,file.readline().split())) for _ in range(n)]
    solution()