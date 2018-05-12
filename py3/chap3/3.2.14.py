# Introducing Python
# 3.2.14 존재여부 확인하기 : in

list1 = ["hyosung", "samsung", "KBS", "topfield", "LG"]
list2 = ["(1) windows CE", "(2) embedded linux", "(3) Android"]
list3 = ["student", "soldier", "engineer"]

result = "student" in list3
print (result)

result = "sckim" in list3
print (result)

# 3.2.15 : 값이 얼마나 있는지 세기 count()
print (list1.count('hyosung'))

# join() refer to 2.3.10 (page 66) & 3.2.16 (page 82)
list1_string = '--'.join(list1)
print (list1_string)