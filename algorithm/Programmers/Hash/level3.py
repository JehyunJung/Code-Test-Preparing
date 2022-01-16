def solution(genres, plays):
    answer = []
    musics=dict()
    index=-1
    for genre, play in zip(genres,plays):
        index+=1
        if genre in musics.keys():
            musics[genre].append((play,index))
        else:
            musics[genre]=[(play,index)]
    
    for value in musics.values():
        value.sort(key=lambda x : (-x[0],x[1]))
    genre_sorted=[]

    for key in musics.keys():
        sub_sum=0
        for plays,index in musics[key]:
            sub_sum+=plays
        genre_sorted.append((sub_sum,key))

    genre_sorted.sort(reverse=True)
    
    for temp,genre in genre_sorted:
      for index in range(min(2,len(musics[genre]))):
          answer.append(musics[genre][index][1])
    
    return answer
if __name__=="__main__":
  genres=[]
  plays=[]

  with open("level3.txt","r") as file:
    genres=list(map(str,file.readline().split()))
    plays=list(map(int,file.readline().split()))
    
  print(solution(genres,plays))