import sys
sys.path.append('../Challenge-1/')
sys.path.append('../Challenge-2/')
from hexTobase64 import hexTobase64
from fixedXOR import fixedXOR

freqs = {
    'a': 0.0651738, 'b': 0.0124248,'c': 0.0217339, 'd': 0.0349835,
    'e': 0.1041442, 'f': 0.0197881,'g': 0.0158610, 'h': 0.0492888,
    'i': 0.0558094, 'j': 0.0009033,'k': 0.0050529, 'l': 0.0331490,
    'm': 0.0202124, 'n': 0.0564513,'o': 0.0596302, 'p': 0.0137645,
    'q': 0.0008606, 'r': 0.0497563,'s': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903,'w': 0.0171272, 'x': 0.0013692,
    'y': 0.0145984, 'z': 0.0007836,
    ' ': 0.1918182 
}

def score(phrase):
	phrase = phrase.lower()
	return sum([freqs[x] for x in phrase if x in freqs.keys()])

def bruteForceXOR(inData):
	maxScore = 0
	res = ""
	for x in range(0, 256):
		xorToTry = str(x) * len(inData)
		transformedData = fixedXOR(inData, xorToTry).decode("hex")
		if score(transformedData) > maxScore:
			maxScore = score(transformedData)
			res = transformedData
	return res
