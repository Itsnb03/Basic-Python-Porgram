l = [1,1,2,3,3,3,5]
mydict={}
for elem in l:
    if elem not in mydict:
        mydict[elem]=1
    else:
        mydict[elem]=mydict[elem]+1;
print(mydict)