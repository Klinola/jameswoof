from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii
import json
import time
import requests

def post_request(token, url, extra_headers=None, custom_data=None):
    headers = {
        "Authorization": "Bearer " + token,
    }
    
    if extra_headers:
        headers.update(extra_headers)

    data = {
        "sign": generate_signature(token, custom_data)
    }
    url = "https://api.jameswoof.com" + url
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    return response

def get_request(token, url, extra_headers=None, custom_data=None):
    headers = {
        "Authorization": "Bearer " + token,
    }
    
    if extra_headers:
        headers.update(extra_headers)
    sig = generate_signature(token, custom_data)
    url = "https://api.jameswoof.com" + url + "?sign=" + sig
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return response

def aes_encrypt(data, key):
    key_bytes = key.encode('utf-8')
    data_bytes = data.encode('utf-8')
    iv = key_bytes
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data_bytes) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    return binascii.hexlify(encrypted).decode('utf-8')

def aes_decrypt(encrypted_data, key):
    key_bytes = key.encode('utf-8')
    iv = key_bytes
    encrypted_data_bytes = binascii.unhexlify(encrypted_data)
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    return decrypted_data.decode('utf-8')

def generate_signature(token, custom_data=None | dict):
    uuid = get_timestamp(13)
    params = {'uuid': uuid}
    if custom_data:
        params = custom_data
    data = json.dumps(params, separators=(',', ':'))
    key = token.split('-')[0][:16]
    signature = aes_encrypt(data, key)
    return signature

def decrypt_signature(token, data):
    key = token.split('-')[0][:16]
    decrypted_data = aes_decrypt(data, key)
    return decrypted_data

def decrypt_response(token, data):
    key = token.split('-')[2][:16]
    decrypted_data = aes_decrypt(data, key)
    return decrypted_data

def get_timestamp(n=13):
    if n == 10:
        return int(time.time())
    elif n == 13:
        return int(time.time() * 1000)
    else:
        raise ValueError("Timestamp length must be either 10 or 13")
