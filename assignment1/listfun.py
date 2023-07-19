# count function

# l=[10,20,30,40,10,10,50,50,20,40,60]
# print(l.count(10))

# print(l.count(40))

# l=["sai","ravi","kumar","sai"]
# print(l.count("sai"))

# l=["sai","ravi","kumar","sai"]
# print(l.count("kumar"))

# l=["sai","ravi","kumar","sai"]
# print(l.count("raj"))


# l="sai","ravi","kumar","sai"
# print(l.count("sai"))

# index function

# l=[10,20,30,40,10,10,50,50,20,40,60]
# print(l.index(10))
# print(l.index(10))
# print(l.index(40))

# print(l.index(100))
# print(l.index(40))

# l=["sai","ravi","kumar","sai"]
# print(l.index("sai"))

# print(l.index("s"))

# print(l.index("saaai"))

# append function

# l = [1, 2, 3]
# l.append(4)
# print(l) 

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.append(l2)
# print(l1)  

# l= [1, 'hello', 3.14, True]
# l.append('world')
# print(l) 


# l=[10,20,30,40,10,10,50,50,20,40,60]
# l.append(90)
# print(l)


# l=["sai","ravi","kumar","sai"]
# l.append("ram")
# print(l)

# insert function

# l = [1, 2, 3]
# l.insert(0, 0)
# print(l) 

# l = [1, 2, 3]
# l.insert(1, 1.5)
# print(l)  

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.insert(1, l2)
# print(l1)  

# l=["sai","ravi","kumar","sai"]
# l.insert(2,"rajesh")
# print(l)

# l = [1, 2, 3]
# l.insert(1, 'hello')
# print(l) 

# extend function

# list = [1, 2, 3]
# list2= [4, 5, 6]
# list.extend(list2)
# print(list) 

# list = [1, 2, 3]
# tuple = (4, 5, 6)
# list.extend(tuple)
# print(list)  

# list = [1, 2, 3]
# str = "hello"
# list.extend(str)
# print(list)  

# list = [1, 2, 3]
# set = {4, 5, 6}
# list.extend(set)
# print(list)  

# list = [1, 2, 3]
# l2 = [4, 'hello', True]
# list.extend(l2)
# print(list)  

#sort function

# l = [5, 2, 9, 1, 5, 6]
# l.sort()
# print(l)  

# fruits = ["banana", "apple", "orange", "kiwi"]
# fruits.sort()
# print(fruits)  

# s = [("John", 25), ("Alice", 19), ("Bob", 22)]
# s.sort(key=lambda x: x[1])
# print(s)  

# s = [("John", 25), ("Alice", 19), ("Bob", 22)]
# s.sort(key=lambda x: x[0])
# print(s)  

# fruits = ["Banana", "Apple", "orange", "kiwi"]
# fruits.sort()
# print(fruits)  

# reverse function

# n = [1, 2, 3, 4, 5]
# n.reverse()
# print(n)  

# fruits = ["apple", "banana", "orange", "kiwi"]
# fruits.reverse()
# print(fruits)  

# fruits = ["Banana", "Apple", "orange", "kiwi"]
# fruits.reverse()
# print(fruits)  

# l = [(1, 'a'), (2, 'b'), (3, 'c')]
# l.reverse()
# print(l)  

# n = [1, 2, 3, 4, 5]
# s = n[::-1]
# print(s)  
# print(n)  

# remove function

# list = [1, 2, 3, 4, 2, 5]
# list.remove(2)
# print(list)  

# fruits = ["apple", "banana", "orange", "apple"]
# fruits.remove("apple")
# print(fruits) 

# list = [1, 2, 3, 4, 2, 5]
# list.remove(1)
# print(list) 

# s = [("John", 25), ("Alice", 19), ("Bob", 22)]
# s.remove("John")
# print(s)

# s = [("John", 25), ("Alice", 19), ("Bob", 22)]
# s.remove(("John",25))
# print(s)

# pop function

# list = [1, 2, 3, 4, 5]
# l = list.pop()
# print(l)  
    
# list = [1, 2, 3, 4, 5]
# s = list.pop(2)
# print(s)  

# fruits = ["apple", "banana", "orange", "apple"]
# fruits.pop(3)
# print(fruits) 


# fruits = ["Banana01", "Apple2", "3orange", "4kiwi"]
# fruits.pop(3)
# print(fruits) 

fruits = ["Banana01", "Apple2", "3orange", "4kiwi",20,30,50]
fruits.pop(3)
print(fruits)
