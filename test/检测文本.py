import re

with open('test/待检测文本.txt','r') as f:
    line = f.readline()
    res = re.findall(r'((\d+(\.\d+)?)\% \{(.*?)\})', line)
    num_old = 0
    que_old = 0
    for i,k in enumerate(res):
        # 测试数字
        if num_old<=float(k[1]):
            # print(float(k[1])-num_old)
            num_old = float(k[1])
        else:
            print('num not order %d'%float(k[1]))
            # raise Exception('num not order')
        # 测试资源
        # print(k[3])
        res2 = re.search(r'.+/(.+)\).*$',k[3])
        # res2 = re.search(r'(\d+(\.\d+)?)\%',k)
        res3 = re.search(r'(\d+)\.png',res2.group(1))
        # print(int(res3.group(1)))
        if que_old<=int(res3.group(1)):
            # print(que_old-int(res3.group(1)))
            que_old= int(res3.group(1))
        else:
            print('[%f] %s next should be %d'%(float(k[1]),k[3],que_old))
            # raise Exception('err que %s'% k[3])
        
        # print(res2.group(1))
        # break