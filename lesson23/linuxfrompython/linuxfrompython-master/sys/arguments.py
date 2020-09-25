import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print(f'Function name {sys.argv[0]}')
    else:
        print(f'Argument {i} name: {sys.argv[i]} ,type: {type(sys.argv[i])}')
