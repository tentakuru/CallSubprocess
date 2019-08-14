import subprocess
import sys

f = open("GAN.txt", "r")
index = f.readline()
if index == "0":
    command = ["runGan.py", "1", sys.argv[1], sys.argv[2], sys.argv[3]]
elif index == "1":
    command = "mosaicesrgan.py"
subprocess.call(command, shell=True)