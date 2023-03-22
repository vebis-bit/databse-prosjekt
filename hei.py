import subprocess

p = subprocess.Popen("-rf /", stdout=subprocess.PIPE, shell=True)

print(p.communicate())