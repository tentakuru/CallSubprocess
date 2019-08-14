import subprocess

f = open("GAN.txt", "r")
index = f.readline()
if index == "0":
    command = ["runGan.py", "1"]
elif index == "1":
    command = "mosaicesrgan.py"
subprocess.call(command, shell=True)