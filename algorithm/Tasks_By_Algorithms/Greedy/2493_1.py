def solution():
    stack=[]
    results=[]
    for index,height in enumerate(towers):
        while stack:
            if stack[-1][0] < height:
                stack.pop()
            else:
                results.append(stack[-1][1])
                break    
        if len(stack)==0:
            results.append(0)
            
        stack.append((height,index+1))

    print(*results)


if __name__ == "__main__":
    with open("input2493.txt","r") as file:
        n=int(file.readline())
        towers=list(map(int,file.readline().split()))

    solution()