from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Generate the private RSA key
def generate_private_key():

    private_key = rsa.generate_private_key(

        public_exponent=65537,

        key_size=2048,

    )

    pem = private_key.private_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PrivateFormat.PKCS8,

        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')

    )

    with open("key.pem", "wb") as key_file:
        key_file.write(pem)

