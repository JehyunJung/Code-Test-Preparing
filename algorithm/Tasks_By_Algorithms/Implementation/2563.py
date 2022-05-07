def solution():
    map=[[0] *100 for _ in range(100)]
    coverage=0
    for start_x,start_y in points:
        for i in range(start_x,start_x+10):
            for j in range(start_y, start_y + 10):
                map[j][i]=1

    for i in range(100):
        coverage+=sum(map[i])
    return coverage
if __name__ == "__main__":
    num=0
    points=[]

    with open("input2563.txt","r") as file:
        num=int(file.readline())
        points=[list(map(int,file.readline().split())) for _ in range(num)]
    print(solution())