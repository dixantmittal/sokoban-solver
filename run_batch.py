import os

low = 450
high = 900

num_iter = 15
batch_size = (high - low)//num_iter

i = low

while i < high :
    print(i, i+batch_size)
    os.system("python x.py {} {}".format(i, i+batch_size))
    i = i+batch_size

