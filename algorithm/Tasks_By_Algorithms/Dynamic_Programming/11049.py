from math import inf
def solution():
    sub_sum=0
    new_list=matrices
    while len(new_list) >1:
        min_index=0
        min_value=inf
        for i in range(len(new_list)-1):
            temp=new_list[i][0]*new_list[i][1]*new_list[i+1][1]
            if temp < min_value:
                min_index=i
                min_value=temp
        sub_sum+=min_value
      
        start=new_list[:min_index]
        middle=[new_list[min_index][0],new_list[min_index+1][1]]
        end=new_list[min_index+2:]
      
        new_list=[]
      
        if len(start)>=1:
            new_list=start
        new_list.append(middle)
        if len(end)>=1:
            new_list.extend(end)
          
    print(sub_sum)      
if __name__ == "__main__":
    num=0
    matrices=[]
    with open("input11049.txt","r") as file:
        num=int(file.readline())
        matrices=[list(map(int,file.readline().split())) for _ in range(num)]
    solution()