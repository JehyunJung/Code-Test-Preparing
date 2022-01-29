from itertools import permutations
def solution(numbers):
    answer = 0
    candidates=[]
    for length in range(1,len(numbers)+1):
        for permutation in list(permutations(list(numbers),length)):
            candidates.append(int(''.join(permutation)))
        
    candidates=set(candidates)
    print(candidates)
    for candidate in candidates:
        count=0
        for i in range(1,candidate+1):
            if candidate%i==0:
                count+=1
                
            if count>3:
                break
        
        if count==2:
            answer+=1
    
    return answer

if __name__== "__main__":
  numbers=""
  with open("level2_1.txt","r") as file:
    numbers=file.readline()
  print(solution(numbers))