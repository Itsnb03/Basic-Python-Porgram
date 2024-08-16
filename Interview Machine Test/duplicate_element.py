lst=[1,3,4,5,3,5,6,6,6,6]
new_lst=[]
for data in lst:
    if data in lst:
        new_lst.append(data)
print(new_lst)