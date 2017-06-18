import subprocess

p = subprocess.Popen(r"C:\Program Files\R\R-3.4.0\bin\R", shell=True)
output = p.communicate(input="floor(4.3)")
print(output)
