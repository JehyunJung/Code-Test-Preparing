from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights=deque(truck_weights)
    
    passing=[0] * bridge_length
    current_weight=0
    while passing:
        answer+=1
        current_weight-=passing.pop(0)
        
        if truck_weights:
            if (current_weight+truck_weights[0]) <= weight:
                passing.append(truck_weights.popleft())
                current_weight+=passing[-1]
            else:
                passing.append(0)
                               
    return answer
    
if __name__ == "__main__":
  bridge_length=0
  weight=0
  truck_weights=[]

  with open("level2_3.txt","r") as file:
    bridge_length=int(file.readline())
    weight=int(file.readline())
    truck_weights=list(map(int,file.readline().split()))
      
  print(solution(bridge_length, weight,truck_weights))