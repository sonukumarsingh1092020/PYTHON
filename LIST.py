list1=[1,2,4,5,7]
list2=["sonu","sudhanshu","aman","rahul" ]
print(list1)
print(list2)
print(list1[1::2])

print(list2[::2])


#list concatination 
list3=list1+list2
print(list3)

print(list2[::2])


#using append in list (used to add new item in the list)
list3.append('satyam')
print(list3)

#removing items from the list 
list3.remove('aman')
print(list3)


#POP COMMAND IS USED TO POP OUT THE LAST ITEM FROM THE LIST 
list3.pop()
print(list3)


#USING INDEXING TO POP COMMAND OUT OF THE LIST
list3.pop(2)
print(list3)
list3.pop(-2)
print(list3)

#sorting in list
list4 = ['a','e','i','o','u' ,'p']
list4.sort()
print(list4)

#REVERSEING IN LIST
list4.reverse()
print(list4)
