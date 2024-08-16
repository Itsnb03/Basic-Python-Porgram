def find_e(list1,list2):
    common_e=[]
    for item in list1:
        if item in list2:
            common_e.append(item)
    return find_e
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common=find_e(list_a,list_b)
print(common)
