import sys
sys.path.append('../Challenge-3/')
sys.path.append('../Challenge-2/')
from xorCipher import score 
from fixedXOR import fixedXOR 

def getScoreFromBruteForceXOR(inData):
	maxScore = 0
	res = ""
	for x in range(0, 256):
		xorToTry = str(x) * len(inData)
		transformedData = fixedXOR(inData, xorToTry).decode("hex")
		if score(transformedData) > maxScore:
			maxScore = score(transformedData)
			res = transformedData
	return maxScore 

with open("data.txt") as f:
	data = f.readlines()
	maxScore = 0
	res = ''
	for x in data:
		if (getScoreFromBruteForceXOR(x.replace('\n', '')) > maxScore):
			maxScore = getScoreFromBruteForceXOR(x.replace('\n', ''))
			res = x.replace('\n', '')
	print res
	print res.decode('hex')
