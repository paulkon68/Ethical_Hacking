import socket
from cryptography.hazmat.primitives import serialization
from gen_priv_key import generate_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


target_host = '127.0.0.1'
target_port = 8000

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

message = b"Sp3ctr3 is 3v3rywh3r3"

with open("key.pem", "rb") as key_file:

    private_key = serialization.load_pem_private_key(

        key_file.read(),

        password=b'mypassword'

    )

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

# send some data
client.send(ciphertext)

# receive some data
response = client.recv(1024)

print(response.decode())

client.close()
