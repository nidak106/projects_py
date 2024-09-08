
q1=input("which is capital city of pakistan? ")
q2=input("which is national flower of pakistan? ")
q3=input("which is national game  of pakistan? ")
ans=[]
ans.append(q1.lower())
ans.append(q2.lower())
ans.append(q3.lower())
right_ans=["islamabad","jasmine","hockey"]

marks=set(ans) & set(right_ans)
marks_count=len(marks)
print(f"total rigth ans are {marks_count}")