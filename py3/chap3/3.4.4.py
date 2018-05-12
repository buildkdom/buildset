# {} is for dictionary of python
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Plain': 'Michael',
}

print (pythons)

pythons['Sungchan'] = 'Kim'
print (pythons)

# adding Seo dong hoon
pythons['Donghoon'] = "Seo"
print (pythons)

# updating Donghoon as Lee dong hoon
pythons['Donghoon'] = "Lee"
print (pythons)
print ("key:", list (pythons.keys()))
print ("values", list(pythons.values()))
# update
others = {"Cleese": "Groucho", "Howard":"Moe"}

# 원래 추가가 되어 있는 key를 이용하면 value를 업데이트 할 수 있고,
# update parameter 값이 원래 존재한 적이 없다면, key value를 추가하게 된다
pythons.update(others)
print (pythons)

print ("key:", list (pythons.keys()))
print ("values", list(pythons.values()))

print ("--------------deleting clesse from dict------------------")
del pythons["Cleese"]
print (pythons)


print ("key:", list (pythons.keys()))
print ("values", list(pythons.values()))


print ("(6) deleting every elements from dictionary using clear() function")
pythons.clear()
print (pythons)
