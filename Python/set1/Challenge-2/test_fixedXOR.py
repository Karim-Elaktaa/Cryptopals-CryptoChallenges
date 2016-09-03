import unittest
from fixedXOR import fixedXOR 

class TestfixedXOR(unittest.TestCase):

	def test_fixedXOR(self):
		intputData = "1c0111001f010100061a024b53535009181c"
		xorData = "686974207468652062756c6c277320657965"
		output = "746865206b696420646f6e277420706c6179"
		self.assertEqual(output, fixedXOR(intputData, xorData))

if __name__ == '__main__':
	unittest.main()
