# page 98
drinks = {
    "martini": {'vodca', 'vermouth'},
    'black russian': {'vodca', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodca'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'scrwedriver': {'orange juice', 'vodca'},
}


print ("-(1)----------")
for name, contents in drinks.items():
    if 'vodca' in contents and not ('vermouth' in contents):
        print (contents)

print ("-(2)----------")
for name, contents in drinks.items():
    # 만약 contents에 vermouth나 orange juice가 있으면 drinks dict의 name을 출력.
    if contents & {'vermouth', 'orange juice'}:
        print (name)