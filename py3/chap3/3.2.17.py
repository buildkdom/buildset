# Introducing Python
# 3.2.17 정렬하기: sort()

list1 = ["hyosung", "samsung", "KBS", "topfield", "LG"]
list2 = ["(1) windows CE", "(2) embedded linux", "(3) Android"]
list3 = ["student", "soldier", "engineer"]

#
# python internal sorted()
#
reference = sorted(list3)
print (list3)
print (reference)

print ('----------------------------------------')
# list.sort()
list3.sort()
print (list3)

list3.sort(reverse=True)
print (list3)

# len() ...
print (len(list3))

# pydoc 을 출력하는 방법. help 안에 자료형 variable 을 입력한다.
# print (help(list3))


things = ["mozzarella", "cinderella", "salmonella"]
print (things[0].capitalize())