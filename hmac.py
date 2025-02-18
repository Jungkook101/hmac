import hmac
import hashlib
import base64

def compute_hmac(message, secret_key):
    hash_algorithm = hashlib.sha256  # No parentheses here

    hmac_object = hmac.new(secret_key.encode(), message.encode(), hash_algorithm)  # Fix

    hmac_digest = hmac_object.digest()

    encode_hmac = base64.b64encode(hmac_digest).decode()
    return encode_hmac

message = "Banh Mi Thit Nuong!"
secret_key = "mySecretKey"

hmac_result = compute_hmac(message, secret_key)
print("HMAC:", hmac_result)
