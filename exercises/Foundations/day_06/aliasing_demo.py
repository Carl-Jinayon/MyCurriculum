# Creates a list
a = [1,2,3]
# B points to the same object as a pointing to
b = a
# In this part the program tries to change the value of the object in the said index.
b[0] = 99
# Here you can see that the actual object is changed.
print(a)

# To do that safely, you need to copy first the original so that it won't be changed.
a = [1,2,3]
b = a[:] 
b[0] = 99
print(a)