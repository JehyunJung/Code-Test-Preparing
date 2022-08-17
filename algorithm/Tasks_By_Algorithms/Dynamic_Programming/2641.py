from bisect import bisect_left
""" def solution():
    di=[1] * (num)

    for i in range(num):
        for j in range(i):
            if students[j] < students[i]:
                di[i]=max(di[i],di[j]+1)

    print(di)
    return num-max(di) """

def solution():
    L=[students[0]]

    for i in range(1,num):
        if L[-1] < students[i]:
            L.append(students[i])

        else:
            index=bisect_left(L,students[i])
            L[index]=students[i]
    
    return num-len(L)
 
if __name__ == "__main__":
    num=0
    students=[]

    with open("input2641.txt","r") as file:
        num=int(file.readline())
        for _ in range(num):
            students.append(int(file.readline().strip()))
    print(solution())
        