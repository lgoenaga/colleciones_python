
fruits = []
fruits.push('apple')
fruits.push('cherry')
fruits.push('banana')
print(fruits) # ['apple', 'cherry', 'banana']
fruits.sort() 
print(fruits) # ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits) # ['apple', 'banana']
fruits.insert(1, 'orange')
print(fruits) # ['apple', 'orange', 'banana']
fruits.remove('orange')
print(fruits) # ['apple', 'banana']
fruits.append('kiwi')
print(fruits) # ['apple', 'banana', 'kiwi']
fruits.append('cherry')
print(fruits) # ['apple', 'banana', 'kiwi', 'cherry']
fruits.sort()
print(fruits) # ['apple', 'banana', 'cherry', 'kiwi']
fruits.pop(2)
print(fruits) # ['apple', 'banana', 'kiwi']
