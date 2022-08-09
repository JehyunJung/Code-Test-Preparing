def solution():
    x,y=0,1
    zero_point=points[0]
    points.append(zero_point)

    plus,minus=0,0

    for i in range(num):
        plus+=(points[i][x]*points[i+1][y])
        minus+=(points[i][y]*points[i+1][x])
    area=0.5*(abs(plus-minus))
    print(round(area,1))

if __name__ == "__main__":
    num=0
    points=[]

    with open("input2166.txt","r") as file:
        num=int(file.readline())
        points=[list(map(int,file.readline().split())) for _ in range(num)]
    solution()