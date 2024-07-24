from base64_encoder.encoder import encode_payload
from base64_encoder.decoder import decode_payload

payload = "Hello, World!"
salt_key = "s3cr3t"
salt_index = 5

encoded = encode_payload(payload, salt_key, salt_index)
print("Encoded payload:", encoded)

decoded = decode_payload(encoded, salt_key, salt_index)
print("Decoded payload:", decoded)

# Testing with incorrect salt index
incorrect_index = 4
decoded_incorrect_index = decode_payload(encoded, salt_key, incorrect_index)
print("Decoded with incorrect index:", decoded_incorrect_index)

# Testing with incorrect salt key
incorrect_salt_key = "wrong_key"
decoded_incorrect_key = decode_payload(encoded, incorrect_salt_key, salt_index)
print("Decoded with incorrect key:", decoded_incorrect_key)
