def solution():
  channel_changes=abs(target_channel-100)
  remaining_buttons=set([str(i) for i in range(0,10) if i not in broken_button_array])

  for num in range(10000001):
    checked=True
    for element in list(str(num)):
      if element not in remaining_buttons:
        checked=False
        break
        
    if checked:
      channel_changes=min(channel_changes,(len(str(num))+abs(target_channel-num)))
    
  return channel_changes
      
if __name__ == "__main__":
  target_channel=0
  broken_buttons=0

  broken_button_array=[]

  with open("input1107.txt","r") as file:
    target_channel=int(file.readline())
    broken_buttons=int(file.readline())
    broken_button_array=list(map(int,file.readline().split()))
  
  print(solution())
