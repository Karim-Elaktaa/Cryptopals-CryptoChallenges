def encryptXor(phrase, KEY = b"ICE"):
	res = ""
	for x in range (len(phrase)):
		tmp = ord(phrase[x]) ^ ord(KEY[x % len(KEY)])
		res += chr(tmp).encode('hex')
	return res
