# Introducing Python
# 3.2.16 문자열로 변환하기 : join()

list1 = ["hyosung", "samsung", "KBS", "topfield", "LG"]
list2 = ["(1) windows CE", "(2) embedded linux", "(3) Android"]
list3 = ["student", "soldier", "engineer"]


# ["hyosung", "samsung", "KBS", "topfield", "LG"]
print (list1)

# hyosung*samsung*KBS*topfield*LG
result = "*".join(list1)
print (result)

# ["hyosung", "samsung", "KBS", "topfield", "LG"]
print (result.split("*"))

# True !!
print (list1 == result.split("*"))