import subprocess

p = subprocess.Popen('brew install sl', stdout=subprocess.PIPE, shell=True)

print(p.communicate())