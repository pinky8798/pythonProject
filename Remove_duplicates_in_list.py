list1=['1','2','3','8','3','1']
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)