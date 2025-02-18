import hmac
import hashlib
import json

# Secret key (must be shared securely between sender and receiver)
SECRET_KEY = b'super_secret_key'

# Sample payload to send
payload = {
    "user": "Steve",
    "amount": 100,
    "timestamp": "2025-02-17T12:00:00"
}

# Convert payload to JSON string
payload_json = json.dumps(payload, sort_keys=True).encode()

# Generate HMAC signature
signature = hmac.new(SECRET_KEY, payload_json, hashlib.sha256).hexdigest()

# Save payload and signature to a file (simulating sending)
with open("message.json", "w") as f:
    json.dump({"payload": payload, "signature": signature}, f)

print("Payload sent and saved with HMAC signature.")
