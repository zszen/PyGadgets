import os
import sys
# import paddle.fluid
import paddlehub as hub 

def check():
    paddle.fluid.install_check.run_check()

def matting():
    humanseg = hub.Module(name="deeplabv3p_xception65_humanseg") 
    path = './image/matting/source/'
    files = []
    dirs = os.listdir(path) 
    for diretion in dirs:
        files.append(path + diretion)
    # deal
    results = humanseg.segmentation(data={"image": files}) 
    for result in results: 
        print(result)
    #     print(result['origin']) 
    #     print(result['processed']) 


print('==dealing==')

# check()
matting()

print('==end==')