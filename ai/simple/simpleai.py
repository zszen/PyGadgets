import random
import math
from functools import reduce

step = 0.001
trainRate = .1
threashold = 0.001
looptime = 0
datas = [[(1,1),1], [(1,0),1], [(0,1),1], [(0,0),0]]
weights = [random.random()-.5 for k in range(3)]
errors = []
maxError=20
def calcError(err):
    errors.append(err)
    if len(errors)>maxError:
        del(errors[0])
    return reduce(lambda x,y: x+y, errors)/len(errors)

def calcOutput(inputs):
    return sigmoid(inputs[0]*weights[0]+inputs[1]*weights[1]+1*weights[2])

def errRate(output, excepted):
    return abs(output-excepted) 

def train(inputs, excepted):
    global looptime, widgets
    err=errRate(calcOutput(inputs), excepted)
    dw = []
    for idx,k in enumerate(weights):
        weights[idx]+=step
        err2 = errRate(calcOutput(inputs),excepted)
        dw.append((err2-err)/step)
        weights[idx]=k
    for idx,k in enumerate(weights):
        weights[idx]-=dw[idx]*trainRate
    e = calcError(err)
    looptime+=1
    if looptime%10000==0:
        print(e)
    return e<threashold

def sigmoid(x):
    return 1/(1+math.pow(math.e, -x))

if __name__ == "__main__":
    for i in range(1000000):
        data = datas[i%len(datas)]
        if train(data[0],data[1]):
            print(f'输出结果: {weights}')
            break
    print('验证：')
    while True:
        ipt = [int(input('bit1: ')), int(input('bit2: '))]
        # weights = [13.13226655111134, 13.132082018425997, -6.107077563222736]
        print(calcOutput(ipt))