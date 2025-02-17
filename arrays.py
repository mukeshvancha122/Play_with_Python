a=[2,3,4,5,6,7]

for i in a:
    print(i)

def add(a):
    res=0
    for i in a:
        res+=i
    return res

b=[5,2,7,3,8,2]
a.extend(b)
print(add(a))
print(a)

a.insert(2,333)
a.append(2121)
print(a)

print(a[1:4])

for i in a[1:4]:
    print(i)

