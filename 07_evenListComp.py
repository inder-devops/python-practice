a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Long way
#even = []
#for i in a:
#    if i % 2 == 0:
#        even.append(i)
#print (even)

# List Comprehension way

print ([i for i in a if i % 2 == 0])