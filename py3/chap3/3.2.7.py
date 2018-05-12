# Introducing Python
# 3.2.7 append()

list1 = ["hyosung", "samsung", "KBS", "topfield", "LG"]
list2 = ["(1) windows CE", "(2) embedded linux", "(3) Android"]
list3 = ["student", "soldier", "engineer"]


# list1.append("Coupang")
# list1.append("Amazon")

# reversing history
# print (list1[::-1])

print (list1[::-1])

# 에러가 발생하지 않는다.
list1.insert(-100, "haha")
list1.insert(100, "haha")
print (list1)