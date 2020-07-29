import quicksort
import shellsort
import numpy as np
import time

list1 = np.random.rand(100000)
list2 = np.random.rand(100000)


t = time.time()
quicksort.quickSort(list2,0,100000-1)
print(time.time()-t)

t = time.time()
shellsort.shellSort(list1)
print(time.time()-t)