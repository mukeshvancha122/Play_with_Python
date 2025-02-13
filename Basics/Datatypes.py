# As other programming language python has built-in datatypes 
"""
Why do we need datatypes? What is the use of it?
-> Datatypes are the catergorization of data.

In python everything deals with objects (datatypes = classes, variables= instance of classes)
Types:

1) Numberic: Integer, float, double, Complex numbers
2) Sequence: String, List, Tuple
3) Mapping: dictionary
4) Boolean: bool
5) Set: sets
"""

#  Numeric
a= type(10)
b= type(20)
c= type(1+2j)

print("Type of a= {0}, b= {1}, c= {2}".format(a,b,c))

# Sequence
d=type([1,2,3,4,5,6])
e=type("Mukesh")
f=type((1,2,3))
# print(len({1,2,3,2}))

print("Type of a= {0}, b= {1}, c= {2}".format(d,e,f))

# dictionary
g={a:"a",b:"b",c:"c"}
print(type(g))