from ..common.checkPrimesRelatively import checkPrimesRelatively
from ..common.multiplicativeInverse import multiplicativeInverse
from ..helpers.fileHelpers import pickFileForEncrypt, pickFileForDecrypt
from sympy import randprime


class RSA:
    @staticmethod
    def generateKeys():
        p = randprime(2**128, 2**156); q = randprime(2**128, 2**156)
        n = p*q; fi = (p-1)*(q-1)
        e = randprime(1, fi)
        while(checkPrimesRelatively(e, fi) != True):
            e = randprime(1, fi)
        d = multiplicativeInverse(e, fi)
        publicKey = {'e': e, 'n': n}; privateKey = {'d': d, 'n': n}
        print('p:', p, 'q:', q, '\nn:', n, 'fi:', fi, '\ne:', e, 'd:', d, '\npublic key:', publicKey, 'private key:', privateKey)
        return publicKey, privateKey


    @staticmethod
    def encrypt(publicKey):
        from progress.bar import Bar

        srcFile, dstFile = pickFileForEncrypt()
        e, n  = int(publicKey['e']), int(publicKey['n'])
        
        with Bar('Processing', max=len(srcFile.read())) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(1)
                if not char: break
                cipherChar = pow(int.from_bytes(char, byteorder='big'), e, n)
                cipherBytes = cipherChar.to_bytes(64, byteorder='big')
                dstFile.write(cipherBytes)
                bar.next()
        srcFile.close(); dstFile.close()


    @staticmethod
    def decrypt(privateKey):
        from progress.bar import Bar

        srcFile, dstFile = pickFileForDecrypt()
        d, n  = int(privateKey['d']), int(privateKey['n'])

        with Bar('Processing', max=len(srcFile.read())/64) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(64)
                if not char: break
                decryptedChar = pow(int.from_bytes(char, byteorder='big'), d, n)
                decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
                dstFile.write(decryptedByte)
                bar.next()
        srcFile.close(); dstFile.close()