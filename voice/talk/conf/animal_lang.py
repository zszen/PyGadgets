import itertools

list1 = ['叽','汪','喵']
list2 = []
# for i in range(1,len(list1)+1):
#     iter = itertools.combinations(list1,i)
#     # print('\n'.join([1,2]))
#     for k in iter:
#         # print(''.join(k))
#         list2.append(''.join(k))
# print(list2)

def dec_to_ter(num):
    l = [] 
    if num < 0:
        return "- " + dec_to_ter(abs(num)) # 负数先转为正数，再调用函数主体
    else:
        while True:
            num,reminder = divmod(num,3) # 算除法求除数和余数
            l.append(str(reminder)) # 将余数存入字符串
            if num == 0:
                return "".join(l[::-1])

for i in range(2024):
    # print(format(i,'b'))
    # list2.append(format(i,'b').replace('0',list1[0]).replace('1',list1[1]))
    list2.append(dec_to_ter(i).replace('0',list1[0]).replace('1',list1[1]).replace('2',list1[2]))
    # list2.append(format(i,'b').replace('0',list1[1]).replace('1',list1[0]))

print(list2)