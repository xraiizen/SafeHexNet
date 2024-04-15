import socket
import binascii
import hashlib

def calculate_checksum(data):
    """ Calcule un checksum MD5 des données. """
    return hashlib.md5(data).hexdigest()

def decode_data(encoded_data):
    """ Décrypte les données reçues. """
    checksum, hex_data = encoded_data.split(':')
    data = binascii.unhexlify(hex_data.encode('utf-8'))
    return checksum, data

def verify_data(encoded_data):
    """ Vérifie les données reçues avec le checksum. """
    received_checksum, data = decode_data(encoded_data)
    calculated_checksum = calculate_checksum(data)
    if received_checksum == calculated_checksum:
        print("Data is valid and intact.")
        print(f"Received data: {data.decode()}")
    else:
        print("Data corruption detected.")

def start_server(host='127.0.0.1', port=65432):
    """ Démarre un serveur TCP qui écoute sur le port spécifié. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                verify_data(data.decode())

start_server()
