import math
# 递归
def a(x, times,*,level=0):
    return x if level>=times-1 else x+a(x*2,times,level=level+1)

# 数学简化
def b(x, times):
    return x*math.pow(2, times)

# 循环
def c(x, times):
    y = 0
    for i in range(times):
        y+=x
        x*=2
    return y

print(a(.01,30)) #10737418.229999999
print(b(.01,30)) #10737418.24
print(c(.01,30)) #10737418.23
