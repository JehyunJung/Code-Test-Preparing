with open("input10828.txt","r") as file:
    n=int(file.readline())
    stack=[]
    for _ in range(n):
        segment=file.readline().strip().split(" ")
        operation=segment[0]
        if operation=="push":
            operand=segment[1]
            stack.append(operand)
        elif operation=="top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif operation=="size":
            print(len(stack))
        elif operation=="empty":
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif operation=="pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        