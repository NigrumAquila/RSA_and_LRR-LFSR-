from ..helpers.fileHelpers import pickFileForEncrypt, pickFileForDecrypt


class LRR:
    NBYTES = 16
    TAPS = (128,126,101,99)

    generateKey = staticmethod(lambda: bin(int.from_bytes(getattr(__import__('os'), 'urandom')(LRR.NBYTES), byteorder='big'))[2:])
    

    @staticmethod
    def generateGamma(shift_register_state):
        xor_input = 1; nbits = shift_register_state.bit_length()
        for tap in LRR.TAPS:
            if (shift_register_state & (1<<(tap-1))) != 0:
                xor_input ^= 1
        shift_register_state = (xor_input << nbits-1) + (shift_register_state >> 1)
        return shift_register_state


    @staticmethod
    def encrypt(seed):
        from progress.bar import Bar

        srcFile, dstFile = pickFileForEncrypt()
        shift_register_state = int(seed, 2)

        with Bar('Processing', max=len(srcFile.read())) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(1)
                if not char: break
                gamma = LRR.generateGamma(shift_register_state)
                shift_register_state = gamma
                cipherChar = gamma ^ int.from_bytes(char, byteorder='big')
                cipherBytes = cipherChar.to_bytes(LRR.NBYTES, byteorder='big')
                dstFile.write(cipherBytes)
                bar.next()
        srcFile.close(); dstFile.close()


    @staticmethod
    def decrypt(seed):
        from progress.bar import Bar

        srcFile, dstFile = pickFileForDecrypt()
        shift_register_state = int(seed, 2)

        with Bar('Processing', max=len(srcFile.read())/(LRR.NBYTES)) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(LRR.NBYTES)
                if not char: break
                gamma = LRR.generateGamma(shift_register_state)
                shift_register_state = gamma
                decryptedChar = gamma ^ int.from_bytes(char, byteorder='big')
                decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
                dstFile.write(decryptedByte)
                bar.next()
        srcFile.close(); dstFile.close()