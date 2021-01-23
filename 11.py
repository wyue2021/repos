# -*- coding: UTF-8 -*-
# print '判断10-30之间的数是否为质数'
# for num in range(10,30):
#     for a in range(2,num):
#         if num%a == 0:
#             b = num/a
#             print'%d 不是质数 %d = %d * %d '%(num,num,a,b)
#             break
#     else:
#         print'%d 是质数'%(num)
print '输出2-100之间的质数'
i = 2
while(i < 100):
    j = 2
    while(j < i/j ):
        if not(i%j):
            break
        j = j+1
    if(j > i/j ):
        print'%d 是质数'%(i)
    i = i+1
