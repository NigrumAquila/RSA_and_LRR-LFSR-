from ..common.primeGenerator import primeGenerator
from ..common.checkPrimesRelatively import checkPrimesRelatively
from ..common.multiplicativeInverse import multiplicativeInverse
from ..helpers.fileHelpers import pickFileForEncrypt, pickFileForDecrypt


class RSA:
    @staticmethod
    def generateKeys():
        p = primeGenerator(2**10, 2**20); q = primeGenerator(2**10, 2**20)
        n = p*q; fi = (p-1)*(q-1)
        e = primeGenerator(1, fi)
        while(checkPrimesRelatively(e, fi) != True):
            e = primeGenerator(1, fi)
        d = multiplicativeInverse(e, fi)
        publicKey = {'e': e, 'n': n}; privateKey = {'d': d, 'n': n}
        print('p:', p, 'q:', q, '\nn:', n, 'fi:', fi, '\ne:', e, 'd:', d, '\npublic key:', publicKey, 'private key:', privateKey)
        return publicKey, privateKey

    @staticmethod
    def encrypt(publicKey):
        srcFile, dstFile = pickFileForEncrypt()
        e, n  = int(publicKey['e']), int(publicKey['n'])

        for char in srcFile.read():
            cipherChar = pow(ord(char), e, n)
            dstFile.write(str(cipherChar) + '\n')
        srcFile.close(); dstFile.close()

    @staticmethod
    def decrypt(privateKey):
        srcFile, dstFile = pickFileForDecrypt()
        d, n  = int(privateKey['d']), int(privateKey['n'])

        for char in srcFile.readlines():
            decryptedChar = pow(int(char.splitlines()[0]), d, n)
            dstFile.write(chr(decryptedChar))
        srcFile.close(); dstFile.close()