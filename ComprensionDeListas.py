l = [1,2,3, -1 ,4]

l2 = [num for num in l if num > 0]
print l
print l2

s = ['H','o','l','a']
l2 = [c * num for c in s
                for num in l
                     if num > 0]

print l2