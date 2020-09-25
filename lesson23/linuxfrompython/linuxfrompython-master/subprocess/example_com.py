import subprocess
from time import sleep

# ---------------
# args = ["ping", "-c 4", "ya.ru"]
# process = subprocess.Popen(args)
# sleep(3)
# out = process.communicate()
#
# print('output: ', out)


# ---------------
# stdout view

# args = ["ping", "-c 4", "ya.ru"]
# process = subprocess.Popen(args, stdout=subprocess.PIPE)
# sleep(3)
# out = process.communicate()
#
# print('output: ', out)


# ---------------
# stdout without stderr
# DEVNULL

# args = ["ping", "-c 4", "info12245.ru"]
# process = subprocess.Popen(args, stderr=subprocess.PIPE)
# sleep(3)
# out = process.communicate()
#
# print('output: ', out)


# ---------------
# stderr view
# args = ["ping", "-c 4", "info12245.ru"]
# process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# sleep(3)
# out = process.communicate()
#
# print('output: ', out)


# ---------------
# output into file

# file = open("ping.txt", "w")
# file_err = open("ping_err.txt", "w")
# args = ["ping", "-c 4", "ya.ru"]
# process = subprocess.Popen(args, stdout=file, stderr=file_err)
# sleep(3)
# out = process.communicate()
#
# print('output: ', out)
# file.close()


# ---------------
# stdin
f = open('search.txt', 'r')
process = subprocess.Popen(['grep', 'test'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process.stdin.write(b"test1\ntest2")
out = process.communicate()
print('output: ', out)
