import sys
sys.path.append('../Challenge-1/')
from hexTobase64 import hexTobase64

def fixedXOR(inData, xorData):	
	return ''.join(format((int(inData[x], 16) ^ int(xorData[x], 16)), 'x') for x in range(0, len(inData)))
