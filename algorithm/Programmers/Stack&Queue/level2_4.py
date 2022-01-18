from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    while prices:
        target_price=prices.popleft()
        count=0
        for price in prices:
            count+=1
            if target_price > price:
                break
        answer.append(count)
    return answer

if __name__ == "__main__":
  prices=[]
  with open("level2_4.txt","r") as file:
    prices=list(map(int,file.readline().split()))
  
  print(solution(prices))