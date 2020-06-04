class LRR:
    NBYTES = 1
    TAPS = (8,7,6,1)

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
        from ..helpers.pickFile import pickFile
        
        srcFilePath = pickFile()
        dstFilePath = srcFilePath + '.encoded'
        srcFile = open(srcFilePath, 'r')
        dstFile = open(dstFilePath, 'w')
        shift_register_state = int(seed)

        for char in srcFile.read():
            gamma = LRR.generateGamma(shift_register_state)
            shift_register_state = gamma
            cipherChar = gamma ^ ord(char)
            dstFile.write(str(cipherChar) + '\n')
        srcFile.close(); dstFile.close()
    
    @staticmethod
    def decrypt(seed):
        from ..helpers.pickFile import pickFile

        srcFilePath = pickFile()
        dstFilePath = srcFilePath[0:-7] + 'decoded'
        srcFile = open(srcFilePath, 'r')
        dstFile = open(dstFilePath, 'w')
        shift_register_state = int(seed)

        for char in srcFile.readlines():
            gamma = LRR.generateGamma(shift_register_state)
            shift_register_state = gamma
            encodedChar = gamma ^ int(char.splitlines()[0])
            dstFile.write(chr(encodedChar))
        srcFile.close(); dstFile.close()

# print(LRR.generateGamma(10001101))
# print(LRR.generateKey())
# LRR.encrypt('10001101')
# LRR.decrypt('10001101')