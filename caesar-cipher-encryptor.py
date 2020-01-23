def caesarCipherEncryptor(string, key):
    # Write your code here.
	# intialize a list to store the results
	encrypted_str = ''
	# normalize the key by using the modulo operator
	key = key % 26
	
	unicode_val = 0
	# loop through the string
	for char in string:	
		# if the unicode value + key is greater than 122
		if ord(char) + key > 122:	
			# calculate the updated unicode value; which is the result of the modulo operator
			unicode_val = 96 + ((ord(char) + key ) % 122)
		# else
		else:
			# calculate the new unicode value; which would unicode value + key
			unicode_val = ord(char) + key
		# insert the value in the results array
		encrypted_str += chr(unicode_val)
	# return encrypted_str
	return encrypted_str
