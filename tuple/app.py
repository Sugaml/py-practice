# Tuple

#creating tuple
my_tuple=(1,2,3,"four",5.6)

#Accessing tuple element
print(my_tuple[0])

print(my_tuple[3])

#Tuple Slicing
print(my_tuple[1:4])

#Tuple unpacking
a,b,c,d,e=my_tuple
print(a,b,c,d,e)

# #Trying to modify a tuple (Note:: Tuples are immutable)
# my_tuple[0]=10 #Rasises Type Error

#Length of a tuple
print(len(my_tuple))