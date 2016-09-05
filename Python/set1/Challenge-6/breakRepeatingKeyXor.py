data1 = "this is a test"
data2 = "wokka wokka!!!"

def getHammingDistance(a, b):
	tot = 0
	for x in range(len(a)):
		aBinChr = ''.join(format(ord(a[x]), '08b'))
		bBinChr = ''.join(format(ord(b[x]), '08b'))
		print a[x], " = ", aBinChr
		print b[x], " = ", bBinChr
		for y in range(len(aBinChr)):
			if aBinChr[y] != bBinChr[y]:
				tot += 1 
	return tot
print getHammingDistance(data1, data2)
