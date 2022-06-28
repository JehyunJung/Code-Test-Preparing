import os
def solution():
    inclinations=[[1] *2 for _ in range(length)]
    max_length=0
    #0 for incline 1 for decline

    for i in range(length-1):
        if datas[i]<=datas[i+1]:
            inclinations[i+1][0]=(inclinations[i][0]+1)
        if datas[i] >= datas[i+1]:
            inclinations[i+1][1]=(inclinations[i][1]+1)


        max_length=max(max_length,inclinations[i+1][0],inclinations[i+1][1])
    max_length=max(max_length,inclinations[length-1][0],inclinations[length-1][1])
    print(max_length)

if __name__ == "__main__":
    length=0
    datas=[]
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, "input2491.txt")
    with open(filename,"r") as file:
        length=int(file.readline())
        datas=list(map(int,file.readline().split()))
    solution()