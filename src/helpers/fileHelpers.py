from .pickFile import pickFile


def writeKey(key, alg):
    root = 'keys/'; filename = input('Enter filename with key: ')
    
    if alg == 'rsa':
        pubkFile = open(root + alg + '.' + filename +'.pubk', 'w')
        pkFile = open(root + alg + '.' + filename +'.pk', 'w')
        for value in key[0].values(): pubkFile.writelines(str(value) + '\n')
        for value in key[1].values(): pkFile.writelines(str(value) + '\n')
        pubkFile.close(); pkFile.close()

    if alg == 'lrr':
        open(root + alg + '.' + filename + '.pk', 'w').write(key)


def readKey(alg, typeKey = None):
    pathToKey = pickFile()
    key = {}

    if alg == 'rsa':
        fullKey = open(pathToKey, 'r').readlines();
        if typeKey == 'public': key['e'] = fullKey[0].splitlines()[0]
        elif typeKey == 'private': key['d'] = fullKey[0].splitlines()[0]
        key['n'] = fullKey[1].splitlines()[0]
        return key

    elif alg == 'lrr':
        return open(pathToKey, 'r').read()


def pickFileForEncrypt():
    srcFilePath = pickFile()
    dstFilePath = srcFilePath + '.encrypted'
    srcFile = open(srcFilePath, 'r')
    dstFile = open(dstFilePath, 'w')
    return srcFile, dstFile


def pickFileForDecrypt():
    srcFilePath = pickFile()
    dstFilePath = srcFilePath[0:-9] + 'decrypted'
    srcFile = open(srcFilePath, 'r')
    dstFile = open(dstFilePath, 'w')
    return srcFile, dstFile