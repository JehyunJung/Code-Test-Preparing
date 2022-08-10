from collections import deque
def solution():
    refined_datas=datas[1:-1]
    if len(refined_datas) == 0:
        refined_datas=[]
    else:
        refined_datas=refined_datas.split(",")
    refined_datas=deque(refined_datas)
    reverse_flag=0
    
    for command in commands:
        if command == "R":
            reverse_flag+=1
        else:
            if len(refined_datas)==0:
                print("error")
                return
            if reverse_flag %2==1:
                refined_datas.pop()
            else:
                refined_datas.popleft()

    if reverse_flag % 2 == 0:
        print("[" + ",".join(refined_datas) + "]")
    else:
        refined_datas.reverse()
        print("[" + ",".join(refined_datas) + "]")


if __name__ == "__main__":
    commands=""
    num=0
    datas=[]

    with open("input5430.txt","r") as file:
        commands=list(file.readline().strip())
        num=int(file.readline())
        datas=file.readline().strip()
    
    solution()