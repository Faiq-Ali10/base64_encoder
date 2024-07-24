import base64

def encode_payload(payload, salt_key, salt_index):
    payload_with_salt = payload + salt_key
    encoded_payload = base64.b64encode(payload_with_salt.encode()).decode()
    encoded_with_index = encoded_payload[:salt_index] + str(salt_index) + encoded_payload[salt_index:]
    return encoded_with_index
