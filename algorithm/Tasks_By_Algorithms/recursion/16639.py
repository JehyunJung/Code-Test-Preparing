from math import inf
max_result=-inf

def calculate(op1,op2,operator):
    if operator == "+":
        return op1+op2
    elif operator =="-":
        return op1-op2
    elif operator == "*":
        return op1*op2
         
def solution():
    operands=[]
    operators=[]

    for segment in expression:
        if "0"<=segment<="9":
            operands.append(int(segment))
        else:
            operators.append(segment)


    di=[[[0,0] for _ in range(num+1)] for _ in range(num+1)]
    
    for i in range(num+1):
        di[i][i][0]=operands[i]
        di[i][i][1]=operands[i]
    
    for diagonal in range(1,num+1):
        for i in range(num-diagonal+1):
            j=i+diagonal
            tmp=[]
            for k in range(i,j):
                tmp.append(calculate(di[i][k][0],di[k+1][j][0],operators[k]))
                tmp.append(calculate(di[i][k][0],di[k+1][j][1],operators[k]))
                tmp.append(calculate(di[i][k][1],di[k+1][j][0],operators[k]))
                tmp.append(calculate(di[i][k][1],di[k+1][j][1],operators[k]))
            di[i][j][0]=min(tmp)
            di[i][j][1]=max(tmp)


    return max(di[0][num])
if __name__ == "__main__":
    length=0
    expression=""
    num=0


    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\recursion\\input16637.txt","r") as file:
        length=int(file.readline())
        expression=list(file.readline())
        num=length//2 
    print(solution())
   
