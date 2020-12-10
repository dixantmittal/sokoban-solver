import os
import sys
from multiprocessing import Pool


def execute(command):
    print(command)
    os.system(command)


print("Starting index: ", int(sys.argv[1]))
print("Ending index: ", int(sys.argv[2]))
print("Number of workers: ", int(sys.argv[3]))

#print("Compiling classes")
#os.system("javac -d bin src/*.java")

commands = [
    "java -classpath bin DataGenerator levels/{:03d}.txt experts/{:03d}.txt".
    format(i, i) for i in range(int(sys.argv[1]), int(sys.argv[2]))
]
pool = Pool(processes=int(sys.argv[3])).map(func=execute, iterable=commands)
