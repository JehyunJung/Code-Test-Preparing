def solution(n,A,B,C,temp):
    global checked,answer
    if checked:
        return
      
    if n==0:
        if A==0 and B==0 and C==0:
            answer=temp
            checked=True
            return

    if A>0:
        solution(n-1,A-1,B,C,temp+"A")
    if B>0:
        if len(temp)>0:
            if temp[-1] != "B":
                solution(n-1,A,B-1,C,temp+"B")
        else:
            solution(n-1,A,B-1,C,temp+"B")
    if C>0:
        if len(temp)>1:
            if temp[-1] != "C" and temp[-2] != "C":
                solution(n-1,A,B,C-1,temp+"C")
        else:
            solution(n-1,A,B,C-1,temp+"C")
    
if __name__ == "__main__":
    A,B,C=0,0,0
    str=[]
    with open("input14238.txt","r") as file:
        str=list(file.readline())
    for char in str:
        if char =="A":
            A+=1
        elif char=="B":
            B+=1
        else:
            C+=1

    checked=False
    answer=""
    solution(len(str),A,B,C,"")

    if checked:
        print(answer)
    else:
        print(-1)

    