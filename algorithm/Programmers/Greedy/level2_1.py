def solution(name):
    answer = 0
    name=list(name)
    index_list=[i for i,c in enumerate(name) if c != "A"]
    index=0
    length=len(name)
    for i in range(len(index_list)):
      print(index_list,answer)
      for count in range(0,length//2+1):
        temp=index+count
        if temp >= length:
          temp-=length
        
        print(temp,name[temp])
        if temp in index_list:
          if "B"<=name[temp]<="N":
            answer+=(ord(name[temp])-ord("A"))+count
          
          else:
            answer+=(26-(ord(name[temp])-ord("A")))+count

          index_list.remove(temp)
          index=temp
          break

        temp=index-count
        if temp <0:
          temp=length+(index-count)
        print(temp,name[temp])
        if temp in index_list:
          if "B"<=name[temp]<="N":
            answer+=(ord(name[temp])-ord("A"))+count
          
          else:
            answer+=(26-(ord(name[temp])-ord("A")))+count

          index_list.remove(temp)
          index=temp
          break
        
        
    return answer

if __name__ == "__main__":
  name=""
  with open("input2_1.txt","r") as file:
    name=file.readline()
  
  print(solution(name))
