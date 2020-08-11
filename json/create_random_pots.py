import os
import numpy as np
import json
import pyperclip

root = os.path.dirname(__file__)+'/'

pots = np.random.random((2,50,2))
pots*=400



# info = {
#     'data':pots.tolist()
# }
# print("pots", pots.astype(np.float))


print(json.dumps(pots.tolist()))

with open(root+'test.json','w+') as f:
    f.write(json.dumps(pots.tolist()))

# pyperclip.copy(json.dumps(pots.tolist()))