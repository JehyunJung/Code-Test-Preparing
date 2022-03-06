from itertools import combinations
def solution(dwarfs):
  dwarfs.sort()
  for combination in list(combinations(dwarfs,7)):
    if sum(combination)==100:
      combination=map(str,combination)
      print("\n".join(combination))
      break


if __name__ =="__main__":
  dwarfs=[]
  with open("input2309.txt","r") as file:
    for _ in range(9):
      dwarfs.append(int(file.readline()))

  solution(dwarfs)