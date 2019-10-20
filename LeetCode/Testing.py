# import numpy as np
# import matplotlib.pyplot as plt
# # import IPython.display as ipd
# # from scipy import signal
#
# #
# # l = [9, 2, 2, 3, 4, 5, 6]
# #
# # a = set(l)
# #
# #
# # print(a)
#
# #  print(2**31)
#
# import string
#
# output = []
# for i in range(26):
#   output.append([i+1,string.ascii_uppercase[i]])
#
# output = dict(output)
# print(output)

import time
import numpy as np

timeArray = []
count = []
for i in range(3):
    count.append(1)
    t = str(time.ctime(time.time()))
    timeArray.append(t[len(t)-13:len(t)-5])
    time.sleep(1)

# print(timeArray)
np.savetxt('text.txt', [timeArray, count], delimiter=',', fmt="%s")




