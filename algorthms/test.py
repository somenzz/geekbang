import msvcrt
import sys

str1 = ''
while True:
    a = msvcrt.getwche()
    if a =='q':
        break
    str1+=a
    if a == ' ':
        print("")
        sys.stdout.write(str1)
    sys.stdout.flush()
