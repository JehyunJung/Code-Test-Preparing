from disjoin_sets import find_parent_compressed, union_parent

v,e=0,0
parents=[]
with open("input1.txt","r") as file:
  v,e=map(int,file.readline().split())
  parents=[i for i in range(v+1)]
  for _ in range(e):
    option,stu1,stu2=map(int,file.readline().split())

    if option == 0:
      union_parent(parents,stu1,stu2)
    elif option == 1:
      if find_parent_compressed(parents,stu1) == find_parent_compressed(parents,stu2):
        print("YES")
      else:
        print("NO")
