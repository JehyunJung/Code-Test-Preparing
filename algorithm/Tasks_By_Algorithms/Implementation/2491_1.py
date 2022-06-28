import os
def solution():
    max_length=0
    start,end=0,0

    while end < length-1:
        if datas[end] > datas[end+1]:
            start=end+1
        end+=1
        max_length=max(max_length,end-start+1)
    max_length=max(max_length,end-start+1)
    start,end=0,0
    while end < length-1:
        if datas[end] < datas[end+1]:
            start=end
        end+=1
        max_length=max(max_length,end-start+1) 
    max_length=max(max_length,end-start+1)    
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