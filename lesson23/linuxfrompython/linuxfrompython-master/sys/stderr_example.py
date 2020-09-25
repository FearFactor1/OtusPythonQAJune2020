import sys

save_stderr = sys.stderr
file = open('error.txt', 'w')
sys.stderr = file

a = 5 / 0
sys.stderr = save_stderr

file.close()
