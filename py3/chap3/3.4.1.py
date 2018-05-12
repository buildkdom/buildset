# not [], () but {}
# page 89
empty_dict = {}
print (empty_dict)

experience = {
    "hyosung": "non blocking IO based event polling",
    "kbs": "datablock, channel object",
    "topfield": "set top box development",
}

print (experience)
print (experience["hyosung"])

#
# step 1
#
print ("(1)---before converting data into dict")
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print (lol)

print ("(2)---after converted into dict from doubly list")
print (dict(lol), end="\n\n")

#
# step 2
#
print ("(1) print list of tuple")
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print (lot, end="\n\n")

#
# step 3
#
print ("(1)---case of ([,], [,], [,])")
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print (tol)
print ("(2)---dict () for of ([,], [,], [,])")
print (dict(tol), end="\n\n")

#
# step 4
#
los = ['ab', 'cd', 'ef']
print (dict(los))

tos = ('ab', 'cd', 'ef')
print (tos)
print (dict(tos))

# comparison
print (dict(tos) == dict(los))