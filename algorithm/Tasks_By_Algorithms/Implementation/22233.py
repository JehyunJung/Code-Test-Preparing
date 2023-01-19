from collections import defaultdict
def solution():
    print(keywords,notes)
    keyword_count=n
    for note_keywords in notes:
        for keyword in note_keywords:
            if keywords[keyword]==1:
                keywords[keyword]=-1
                keyword_count-=1
        print(keyword_count)


if __name__ == "__main__":
    with open("input22233.txt","r") as file:
        n,m=map(int,file.readline().split())
        keywords=defaultdict(int)
        
        for _ in range(n):
            keyword=file.readline().strip()
            keywords[keyword]=1
        
        notes=[list(map(str,file.readline().strip().split(","))) for _ in range(m)]
    
    solution()
        