import os,sys

from multiprocessing import Process

process_list = []

def func(command) :
    print(command)
    os.system(command)

for i in range(int(sys.argv[1]), int(sys.argv[2])) :
    command = ["java -jar SokobanSolver.jar levels/{}.txt experts/{}.txt".format(i,i)]
    print(command)
    process_list.append(Process(target=func, args=command))

try :
    for p in process_list :
        p.start()
    for p in process_list :
        p.join()
finally :
    for p in process_list :
        p.terminate()
