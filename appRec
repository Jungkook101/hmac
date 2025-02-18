import hmac
import hashlib
import json

# Secret key (must match the sender's key)
SECRET_KEY = b'super_secret_key'

# Load the received payload
with open("message.json", "r") as f:
    data = json.load(f)

# Extract payload and signature
received_payload_json = json.dumps(data["payload"], sort_keys=True).encode()
received_signature = data["signature"]

# Recompute the HMAC signature
expected_signature = hmac.new(SECRET_KEY, received_payload_json, hashlib.sha256).hexdigest()

# Verify authenticity
if hmac.compare_digest(received_signature, expected_signature):
    print("✅ Payload is authentic:", data["payload"])
else:
    print("❌ Warning: Payload has been tampered with!")
