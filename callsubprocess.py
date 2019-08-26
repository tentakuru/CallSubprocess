import subprocess
import sys
import os

f = open("GAN.txt", "r")
index = f.readline()
if index == "0":
    command = ["runGan.py", "1", sys.argv[1], sys.argv[2], sys.argv[3]]
elif index == "1":
    command = ["runGan.py", "1", sys.argv[1], sys.argv[2], sys.argv[3], "tentakuru"]
elif index == "2":
    command = ["mosaicesrgan.py"]
elif index == "3":
    command = ["runGan.py", "1", sys.argv[1], sys.argv[2], "1", sys.argv[3]]  
elif index == "4":
    command = ["runGan104.py", "1", sys.argv[1], sys.argv[2], "0"]    
elif index == "104":
    command = [os.path.dirname(os.getcwd()) + "\\runGan104.py", "1", sys.argv[1], sys.argv[2], "0"]
subprocess.call(command, shell=True)