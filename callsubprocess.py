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
elif index == "5":
    command = ["runGan104.py", "1", sys.argv[1], sys.argv[2], "1"]  
elif index == "6":
    command = ["mosaicesrgan104.py"]   
elif index == "104":
    cwdneedschange = True
    tgpath = "" #copy your path from runGan104.py
    command = [os.path.dirname(os.getcwd()) + "\\runGan104.py", "1", sys.argv[1], sys.argv[2], "0"]
elif index == "102":
    command = ["runGan102.py", "1"]
if cwdneedschange:
    subprocess.call(command, shell=True, cwd=tgpath)
else:
    subprocess.call(command, shell=True)