import unittest
from xorCipher import bruteForceXOR

class TestBruteForceXOR(unittest.TestCase):

	def test_bruteForceXOR(self):
		intputData = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
		output = "Cooking MC's like a pound of bacon"
		self.assertEqual(output, bruteForceXOR(intputData))

if __name__ == '__main__':
	unittest.main()
