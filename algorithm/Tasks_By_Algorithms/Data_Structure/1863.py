def solution():
    stack=[]
    count=0

    for height in height_changes:
        
        #높이가 0인 부분에는 건물이 있을 수 없다.
        if height ==0:
            count+=len(stack)
            stack=[]
        else:
            #top에 본인보다 큰 값이 있는 경우 빼낸다.
            while stack and stack[-1] >= height:
                #만약 크기가 같은 경우에는 건물의 수를 증가시키지는 않는다.
                if stack[-1] != height:
                    count+=1

                stack.pop()
            
            stack.append(height)

        print(f"height:{height},stack={stack},count={count}")
    print(count)
        


if __name__ == "__main__":
    with open("input1863.txt","r") as file:
        n=int(file.readline())
        height_changes=[list(map(int,file.readline().split()))[1] for _ in range(n)]+[0]
    
    solution()