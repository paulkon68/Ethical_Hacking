from cryptography.hazmat.primitives import serialization
from gen_priv_key import generate_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


# Generate the RSA private key
generate_private_key()

# Load the RSA private key
with open("key.pem", "rb") as key_file:

    private_key = serialization.load_pem_private_key(

        key_file.read(),

        password=b'mypassword',

    )


message = b"Sp3ctr3 is 3v3rywh3r3"

public_key = private_key.public_key()

# Encrypt the message using the public key
ciphertext = public_key.encrypt(

    message,

    padding.OAEP(

        mgf=padding.MGF1(algorithm=hashes.SHA256()),

        algorithm=hashes.SHA256(),

        label=None

    )

)

# Decrypt the message

plaintext = private_key.decrypt(

    ciphertext,

    padding.OAEP(

        mgf=padding.MGF1(algorithm=hashes.SHA256()),

        algorithm=hashes.SHA256(),

        label=None

    )

)

# print the decrypted message
print(plaintext)
