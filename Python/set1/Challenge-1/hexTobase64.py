def hexTobase64(inData):
	return inData.decode("hex").encode("base64").replace('\n', '')
