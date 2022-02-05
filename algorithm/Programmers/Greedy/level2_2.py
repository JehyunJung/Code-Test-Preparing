def solution(number, k):
    answer = ''
    
    stack=[]
    count=0
    
    for num in number:
        while count < k and len(stack) !=0 and stack[-1] < num:
            count+=1
            stack.pop()
        stack.append(num)

    answer="".join(stack[:len(number)-k])
    
    return answer

if __name__ == "__main__":
  number=""
  k=0
  with open("input2_2.txt","r") as file:
    number=file.readline()
    k=int(file.readline())
  
  print(solution(number,k))
