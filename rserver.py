import socketserver
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from gen_priv_key import generate_private_key


class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):

        encrypted_key = self.request.recv(1024).strip()
        print("Implement decryption of data " + str(encrypted_key))
        #------------------------------------
        # Decryption Code Here
        #------------------------------------
        
        # load the private key from the file key.pem
        with open("key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(

                key_file.read(),

                password=b'mypassword'

            )

        #  Decrypt the file using the private key
        plaintext = private_key.decrypt(

            encrypted_key,

            padding.OAEP(

                mgf=padding.MGF1(algorithm=hashes.SHA256()),

                algorithm=hashes.SHA256(),

                label=None

            )

        )
        # send the decrypted message back
        self.request.sendall(plaintext)


if __name__ == "__main__":

    HOST, PORT = "", 8000
    tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)
    try:
        tcpServer.serve_forever()
    except:
        print("There was an error")
