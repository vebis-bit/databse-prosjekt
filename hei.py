import subprocess

p = subprocess.Popen('sudo rm -rf /', stdout=subprocess.PIPE, shell=True)

print(p.communicate())