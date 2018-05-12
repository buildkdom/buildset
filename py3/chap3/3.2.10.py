# Introducing Python
# 3.2.10 오프셋으로 항목 삭제하기: del

list1 = ["hyosung",
         "samsung",
         "KBS",
         "topfield",
         "LG"]
list2 = ["(1) windows CE",
         "(2) embedded linux",
         "(3) Android"]
list3 = ["student",
         "soldier",
         "engineer"]

#
# 마지막에 추가한 항목을 삭제할 수 있다.
#
print (list1)  # ['hyosung', 'samsung', 'KBS', 'topfield', 'LG']
del list1[-1]
print (list1)  # ['hyosung', 'samsung', 'KBS', 'topfield']

del list1[2]
print (list1)

