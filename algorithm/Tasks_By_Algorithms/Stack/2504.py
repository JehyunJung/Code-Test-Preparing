def solution(input_string):
  stack=[]

  for string in input_string:
    print(stack)
    if string==")":
      value=0
      while stack:
        print(stack)
        top=stack.pop()
        if top == "(":
          if value==0:
            stack.append(2)
          else:
            stack.append(2*value)
          break
        elif top=="[":
          return 0
        else:
          value+=int(top)
    elif string=="]":
      value=0
      while stack:
        print(stack)
        top=stack.pop()
        if top == "[":
          if value==0:
            stack.append(3)
          else:
            stack.append(3*value)
          break
        elif top=="(":
          return 0
        else:
          value+=int(top)
    else:
      stack.append(string)
  
  value=0
  while stack:
    print(stack)
    top=stack[-1]
    if top =="(" or top=="[":
      return 0
    value+=int(top)
    stack.pop()
  return value
    
      
if __name__ == "__main__":
  input_string=""
  with open("input2504.txt","r") as file:
    input_string=file.readline()
  print(solution(input_string))