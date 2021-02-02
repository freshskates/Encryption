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


if __name__ == "__main__":

    plain = input("Enter phrase to cipher: ")
    key = int(input("Enter key: "))
    print("Original: " + plain)
    print("Cipher: " + Encryption.cipher(plain))
    print("Decipher: " + Encryption.cipher(plain, -1))


# getIndex = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
#           "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

# getChar = {value: key for key, value in getIndex.items()}

# print("".join([getChar[(getIndex[x] + key) % 26] for x in plain.lower()]))
