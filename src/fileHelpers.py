pathToKeys = 'keys/'

def writeKeys(key, alg):
    if alg == 'rsa':
        pkFile = open(pathToKeys + 'rsa.pk', 'w')
        pubkFile = open(pathToKeys + 'rsa.pubk', 'w')
        modulusFile = open(pathToKeys + 'rsa.modulus', 'w')

        for pubkChar in str(key[0]['e']):
            pubkFile.write(pubkChar)
        pubkFile.close()

        for pkChar in str(key[1]['d']):
            pkFile.write(pkChar)
        pkFile.close()

        for modulusChar in str(key[0]['n']):
            modulusFile.write(modulusChar)
        modulusFile.close()

    if alg == 'lrr':
        pkFile = open(pathToKeys + 'lrr.pk', 'w')
        
        for pkChar in str(key):
            pkFile.write(pkChar)
        pkFile.close()

def readKey(alg, typeKey):
    key = {}

    if alg == 'rsa':
        if typeKey == 'public': key['e'] = open(pathToKeys + 'rsa.pubk', 'r').read()
        elif typeKey == 'private': key['d'] = open(pathToKeys + 'rsa.pk', 'r').read()
        key['n'] = open(pathToKeys + 'rsa.modulus', 'r').read()
    
    return key