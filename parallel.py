import os
import sys
from multiprocessing import Pool


def execute(command):
    print(command)
    os.system(command)


print("Starting index: ", int(sys.argv[1]))
print("Ending index: ", int(sys.argv[2]))
print("Number of workers: ", int(sys.argv[3]))

commands = [
    "java -jar bin/SokobanSolver.jar levels/{:03d}.txt experts/{:03d}.txt".
    format(i, i) for i in range(int(sys.argv[1]), int(sys.argv[2]))
]
print(commands)
pool = Pool(processes=int(sys.argv[3])).map(func=execute, iterable=commands)
