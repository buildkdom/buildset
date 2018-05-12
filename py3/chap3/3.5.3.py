# page 98
drinks = {
    "martini": {'vodca', 'vermouth'},
    'black russian': {'vodca', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodca'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'scrwedriver': {'orange juice', 'vodca'},
}


for name, contents in drinks.items():
    print (name, contents)