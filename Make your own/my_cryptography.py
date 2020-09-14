from cryptography.fernet import Fernet

def writeKey():
	with open('key.KEY', 'wb') as f:
		f.write(Fernet.generate_key())

def loadKey():
	with open('key.KEY', 'rb') as f:
		return f.read()


def encrpyt_data(filname, the_key):
	fern = Fernet(the_key)

	with open(filname, 'rb') as f:
		read_data = f.read()

	encrypted = fern.encrypt(read_data)

	with open(filname, 'wb') as f:
		f.write(encrypted)


def decrpyt_data(filname, the_key):
	fern = Fernet(the_key)

	with open(filname, 'rb') as f:
		read_data = f.read()

	decrypted = fern.decrypt(read_data)

	with open(filname, 'wb') as f:
		f.write(decrypted)


#writeKey()

key = loadKey()

#encrpyt_data('someFile.txt', key)
decrpyt_data('someFile.txt', key)