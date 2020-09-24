import sys
import subprocess
import os
'''
if __name__ == '__main__':
    argument = sys.argv
    del argument[0]
'''
'''
def read_file (filename, chunksize=4096):
    with open(sys.argv[1], "rb") as f:
        while True:
            chunk = f.read(chunksize)
'''

defragsize=int(sys.argv[2])

#Variables for selective defragmentation
start=int(sys.argv[3])
end=int(sys.argv[4])
#

frag_degree = open("frag_degree", "w+")
target_file = open(sys.argv[1],"rb+",0)


subprocess.check_call(["filefrag", "-v", sys.argv[1]], stdout=frag_degree)

#Set up the file offset to start
frag_degree.seek(start)
#

frag_degree.readline()
line = frag_degree.readline()
filesize = line.split(' ')[5]
frag_degree.readline()


lines = frag_degree.readlines()


bufsize = 0
need = 0
for line in lines[:-1]:
    #Perform defragmentation until the file offset reaches "end" offset
    if (target_file.tell() >= end)
        break
    #

    fragsize = int(line.split(':')[3])
    bufsize += fragsize * 4
    if bufsize < defragsize:
        need = 1
        continue

    while bufsize >= defragsize:
        if need == 1:
            '''print(need)'''
            data = target_file.read(defragsize*1024)
            size = len(data)
            target_file.seek(-1*size,1)
            target_file.write(data)

            '''os.fsync(target_file.fileno())'''
            need = 0
            target_file.seek(-1*defragsize*1024,1)

        
        target_file.seek(defragsize*1024,1)
        bufsize -= defragsize

    if bufsize > 0:
        need=1

'''print(target_file.tell())'''
if need == 1:
    data = target_file.read(bufsize*1024)
    size = len(data)
    target_file.seek(-1*size,1) 
    target_file.write(data)
    
target_file.flush()
os.fsync(target_file.fileno())

target_file.close()
frag_degree.close()
