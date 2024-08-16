num=[3,54,2,5,64]
for i in range(0,len(num)):
    for j in range(0,len(num)-1):
        if num[j]>num[j+1]:
            big_element=num[j]
            num[j]=num[j+1]
            num[j+1]=big_element
print(num)