# Robert Cacho Ruiz

class Encryption:

    @staticmethod
    def getIndex(character):
        return 26 - (122 - ord(character)) - 1

    @staticmethod
    def getChar(index):
        return chr(97 + index)

    @staticmethod
    def cipher(phrase: str, mode=1) -> str:
        # mode: 1 cipher
        # mode: -1 decipher
        return "".join(Encryption.getChar((Encryption.getIndex(x) + key * mode) % 26) if x.isalpha() else x
                       for x in phrase.lower())

    @staticmethod
    def affine(phrase: str, a, b) -> str:
        return "".join(Encryption.getChar((a * Encryption.getIndex(x) + b) % 26)if x.isalpha() else x
                       for x in phrase.lower())


if __name__ == "__main__":

    plain = input("Enter phrase to cipher: ")
    print("Press 0 for Caesar cipher \npress 1 for Affine Cipher \npress 2 for Brute Force \n")
    option = int(input("Your option : "))
    if(option == 0):
        key = int(input("Enter key: "))
        print("Original: " + plain)
        print("Cipher: " + Encryption.cipher(plain))
        print("Decipher: " + Encryption.cipher(plain, -1))
    elif(option == 1):
        a = int(input("enter a: "))
        b = int(input("enter b: "))
        print("Cipher: " + Encryption.affine(plain, a, b))
