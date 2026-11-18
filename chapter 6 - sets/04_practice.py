# can we have a set with 18(int) and '18'(str) as a value in it 
# yes
# 18 (int) and '18' (str) are considered different elements in a set

s = set()
s.add(18)
s.add('18')
print(s)

# tell length of the following set
a = set()
a.add(20)
a.add(20.0)   # 20 and 20.0 are considered the same element in a set, so the length will be 1 for both
a.add('20')
print(a)
print(len(a))

# the comparison operator == checks for equality of values, not the type of the values.
