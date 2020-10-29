'''
* https://smlee729.wordpress.com/2018/03/14/algorithm-%EB%AC%B8%EC%A0%9C-%EB%8D%A7%EC%85%88%ED%95%98%EC%A7%80-%EC%95%8A%EA%B3%A0-%EB%8D%A7%EC%85%88%ED%95%98%EA%B8%B0/
'''

# MASK = 0xF
# print (bin(-1))
# print (bin(-1 & MASK))

m1 = 0xF
m2 = 0xFFFFFFFF

print (bin(-4 & m1))
print (-4 & m1)
print (bin(4 & m1))
print (bin(-4 & m2))
print (bin(4 & m2))

'''
4비트 체계) 1 1 1 1

-4 & m1
-> 0 1 0 0

-4 & m2
-> 
'''

