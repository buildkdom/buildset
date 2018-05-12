# Introducing Python
# 3.2.11 값으로 항목 삭제하기: remove

list1 = ["hyosung", "samsung",
         "KBS",
         "topfield",
         "LG"]
list2 = ["(1) windows CE",
         "(2) embedded linux",
         "(3) Android"]
list3 = ["student",
         "soldier",
         "engineer"]

#########################################################
# remove() 함수는 별로인 듯 하다.
# 리스트에서 찾고 싶은 값을 찾지 못하면, ValueError 발생한다.
# list.remove(x): x not in list
#

#
# 3.2.12 pop() 오프셋으로 항목을 얻은 후 삭제하기
#
print (list1)
# 가장 뒤에 있는 값을 반환하면서 삭제 처리한다
deleteItem = list1.pop()
print ("deleted item = " + deleteItem)

# 가장 앞에 있는 값을 반환하면서 삭제 처리한다
deleteItem = list1.pop(0)
print ("deleted item = " + deleteItem)