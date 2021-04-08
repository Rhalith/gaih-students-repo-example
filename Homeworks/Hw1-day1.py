my_list = list(range(10))
list1 = my_list[0:5]
list2 = my_list[5:10]
list1, list2 = list2, list1
print (list1,list2)
