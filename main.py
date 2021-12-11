from aes import AES,text2matrix
import os
import numpy as np
import unittest

def hexmatrix(plaintext):
    matrix = text2matrix(plaintext)
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(matrix[i][j])
    return matrix




def main():
    print("EECE 455 Project")
    # plaintext = input("Please input the Message in Hexadecimal: ")
    plaintext = 0x2b7e151628aed2a6abf7158809cf4f3c
    # key = input("Please input the Key in Hexadecimal: ")
    master_key =0x2b7e151628aed2a6abf7158809cf4f3c6bc1bee22e409f96

    # # Output result as a 4x4 matrix:
    # a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    # print("Result: ")
    # for line in a:
    #     print ('  '.join(map(str, line)))


    setUp = AES(master_key,192)


    print('--------------------encryption-----------------------------------')

    encrypted = AES.encrypt(setUp,plaintext)
    roundNum = 0
    for round in encrypted:
        print('--------------------round '+ str(roundNum)+'--------------------')
        print(hex(round))
        matrix = hexmatrix(round)
        print(matrix)
        roundNum+=1





    print('\n--------------------Decryption-----------------------------------')

    decrypted = AES.decrypt(setUp,encrypted[len(encrypted)-1])
    roundNum = 0
    for round in decrypted:
        print('--------------------round '+ str(roundNum)+'--------------------')
        print(hex(round))
        matrixDec = hexmatrix(round)
        print(matrixDec)
        roundNum+=1



    print('\n--------------------Expanded key for all rounds-----------------------------------\n')

    expandedkey = AES.getexpandedkey(setUp)
    for i in range(len(expandedkey)):
        for j in range(len(expandedkey[i])):
            expandedkey[i][j] = hex(expandedkey[i][j])
    print(expandedkey)




    # Wrong Output!

    # os.system("pause")

# class AES_TEST(unittest.TestCase):
#     def setUp(self):
#         master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
#         self.AES = AES(master_key)
#
#     def test_encryption(self):
#         plaintext = 0x3243f6a8885a308d313198a2e0370734
#         encrypted = self.AES.encrypt(plaintext)
#
#         self.assertEqual(encrypted, 0x3925841d02dc09fbdc118597196a0b32)
#
#     def test_decryption(self):
#         ciphertext = 0x3925841d02dc09fbdc118597196a0b32
#         decrypted = self.AES.decrypt(ciphertext)
#
#         self.assertEqual(decrypted, 0x3243f6a8885a308d313198a2e0370734)


if __name__ == "__main__":
    main()
    # unittest.main()
