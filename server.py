import socket
import binascii
import hashlib

def calculate_checksum(data):
    """ Calcule un checksum MD5 des données. """
    return hashlib.md5(data).hexdigest()

def encode_data(data):
    """ Encode les données en hexadécimal. """
    hex_data = binascii.hexlify(data).decode('utf-8')
    checksum = calculate_checksum(data)
    return f"{checksum}:{hex_data}"

def send_data(data, host='127.0.0.1', port=65432):
    """ Envoie des données encodées au serveur. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        encoded_data = encode_data(data)
        s.sendall(encoded_data.encode())
        print("Data sent to server")

# Exemple de données à envoyer
data = b"Hello, world!"
send_data(data)
