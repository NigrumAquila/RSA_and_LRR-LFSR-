from time import sleep
from progress.bar import Bar

file = open('keys/lrr.1.pk.encrypted', 'rb')
# while True:
#     c = file.read(1)
#     if not c: break
#     print(c, end='')
#     sleep(0.1)
    

# numberOfCharacters = len(file.read())
# print(numberOfCharacters)

with Bar('Processing', max=len(file.read())/64) as bar:
    file.seek(0)
    while True:
        c = file.read(16*4)
        if not c: break
        bar.next()