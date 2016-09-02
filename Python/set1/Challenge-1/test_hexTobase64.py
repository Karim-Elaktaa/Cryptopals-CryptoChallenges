import unittest
from hexTobase64 import hexTobase64

class TesthexTobase64(unittest.TestCase):

	def test_hexTobase64(self):
		hexData = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
		base64Data = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
		self.assertEqual(base64Data, hexTobase64(hexData))

if __name__ == '__main__':
	unittest.main()
