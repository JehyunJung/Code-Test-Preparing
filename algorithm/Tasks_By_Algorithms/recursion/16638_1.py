from math import inf

max_result=-inf
def recursion(count,is_Used,expression):
    global max_result

    if count==num:
        if is_Used:
            max_result=max(max_result,eval(expression))
        #마지막 항에 대해서 괄호를 사용하지 않은 경우 마지막 피연산자도 추가한다.
        else:
            max_result=max(max_result,eval(expression+operands[count]))

        return
    #이전에 괄호를 취하지 않은 경우
    if is_Used==False:
        #현재 괄호를 취하는 경우 괄호 계산후에 해당 피연산자항 추가
        recursion(count+1,True,expression+"("+operands[count]+operators[count]+operands[count+1]+")")
        #현재 괄호를 취하지 않는 경우 피연산자와 연사자항 추가
        recursion(count+1,False,expression+operands[count]+operators[count])

    #이전에 괄호를 취한 경우
    else:
        # 연산자만 추가한다.
        recursion(count+1,False,expression+operators[count]) 
         
def solution():

    for segment in expression:
        if "0"<=segment<="9":
            operands.append(segment)
        else:
            operators.append(segment)

    recursion(0,False,"")
    
    print(max_result)
        
if __name__ == "__main__":
    length=0
    expression=""
    num=0
    operands=[]
    operators=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\recursion\\input16637.txt","r") as file:
        length=int(file.readline())
        expression=list(file.readline())
        num=length//2 
    solution()
   
