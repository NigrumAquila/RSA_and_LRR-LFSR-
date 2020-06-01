from src.fileHelpers import writeKeys, readKey


while True:
    case = input('Select action: 1 - RSA; 2 - Linear recurrent register; "e" - to exit: ')
    if case == '1':
        from src.RSA import RSA

        while True:
            case = input('Select action: 1 - Generate keys; 2 - Encode file; 3 - Decode file; "e" - to exit: ')

            if case == '1':
                writeKeys(RSA.generateKeys(), 'rsa')
                print('Keys generated.')

            elif case == '2':
                key = readKey('rsa', 'public')
                data = open('data/text.txt').read()[3:]
                cipher = RSA.encrypt(key, int(data))

                cipherFile = open('data/cipher', 'w')
                for cipherChar in str(cipher):
                    cipherFile.write(cipherChar)
                cipherFile.close()                
                print('File encrypted.', cipher)

            elif case == '3':
                key = readKey('rsa', 'private')
                cipher = open('data/cipher', 'r').read()
                decrypted = RSA.decrypt(key, int(cipher))
                print('File decrypted.', decrypted)

            elif case == 'e':
                exit('Execution completed.')

            else:
                print('Wrong selection. Please, try again.')

    elif case == '2':

        while True:
            case = input('Select action: 1 - Generate key; 2 - Encode file; 3 - Decode file; "e" - to exit: ')

            if case == '1':
                print('Keys generated.')

            elif case == '2':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                print('File encrypted.')

            elif case == '3':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                print('File decrypted.')

            elif case == 'e':
                exit('Execution completed.')

            else:
                print('Wrong selection. Please, try again.')

    elif case == 'e':
        exit('Execution completed.')

    else:
        print('Wrong selection. Please, try again.')
