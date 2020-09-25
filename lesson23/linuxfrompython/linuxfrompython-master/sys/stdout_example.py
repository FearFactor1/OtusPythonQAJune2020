import sys

save_stdout = sys.stdout
file = open('output.txt', 'w')
sys.stdout = file

print('Test info')
sys.stdout = save_stdout

file.close()
