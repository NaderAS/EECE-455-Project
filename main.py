from aes import AES
import os
import numpy as np
import unittest

def main():
    print("EECE 455 Project")
    # plaintext = input("Please input the Message in Hexadecimal: ")
    plaintext = 0x3243f6a8885a308d313198a2e0370734
    # key = input("Please input the Key in Hexadecimal: ")
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c

    # # Output result as a 4x4 matrix:
    # a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    # print("Result: ")
    # for line in a:
    #     print ('  '.join(map(str, line)))

    setUp = AES(master_key)
    encrypted = AES.encrypt(setUp,plaintext)
    decrypted = AES.decrypt(setUp,encrypted)
    print(encrypted)
    print(decrypted)
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
