# s=input("enter the string :") #the boy name is ram
# subs=input("enter the sub string :")
# f=False
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(subs,pos+1,n) #17
#     if pos==-1:
#         break
#     print("found at index : ",pos)
#     f=True
# if f==False:
#     print("not found ")


# replace function

# a= "ram is good boy and intelligent"
# b= a.replace("ram","ravi")
# print(a)
# print(b)  

# b= a.replace("good","bad") 
# print(a)
# print(b)  

# b= a.replace("boy","girl") 
# print(a)
# print(b) 

# b= a.replace("intelligent","hard working") 
# print(a)
# print(b) 

# split function

# a= "10,20,30,40,50,60,70,80,90"
# l= a.split(",",3)
# print(l)
# for i in l:
#     print(i,end=" ")


# a= "10,20,30:40:50,60,70:80:90"
# l= a.split(",",3)
# print(l)


# a= "10,20=30:40=50,60=70:80:90"
# l= a.split("=",3)
# print(l)


# a= "10 20=30 40=50 60=70:80:90"
# l= a.split(" ",3)
# print(l)

# a= "10&20=30&40=50&60=70:80:90"
# l= a.split("&",2)
# print(l)

# find function

# a= "ram is good boy and intelligent"
# b=a.find("ram")
# print(b)

# b=a.find("and")
# print(b)

# b=a.find("sai")
# print(b)

# a=[10,20,40,50,60]
# b=a.find(10)
# print(b)

# a={10,20,40,50}
# b=a.find(10)
# print(b)

# a=["sai","kumar","ravi"]
# b=a.find("ravi")
# print(b)

# index function

# a= "ram is good boy and intelligent"
# b=a.index("ram")
# print(b)

# b=a.index("boy")
# print(b)

# b=a.index("sai")
# print(b)

# a=[10,20,40,50,60]
# b=a.index(10)
# print(b)

# a={10,20,40,50}
# b=a.index(10)
# print(b)

# a=["sai","kumar","ravi"]
# b=a.index("ravi")
# print(b)

# strip function


# a= "ram is good boy,intelligent"
# b=a.strip()
# print(b)

# b=a.strip(",")
# print(b)

# b=a.strip("$")
# print(b)

# a=["sai","kumar","ravi"]
# b=a.strip()
# print(b)

# a={10,20,40,50}
# b=a.strip()
# print(b)

# a= "ram:is:good:boy,intelligent"
# b=a.strip(",")
# print(b)

# b=a.strip(":")
# print(b)

# join function

# a= "ram is good boy intelligent"
# b=",".join(a)
# print(b)

# a=["sai","kumar","ravi"]
# b=":".join(a)
# print(b)

# a=[10,20,40,50,60]
# b=":".join(a)
# print(b)

# a=["sai","kumar","ravi"]
# b="%".join(a)
# print(b)

a=["sai","kumar","ravi"]
b="!".join(a)
print(b)