import base64

def decode_payload(encoded_payload, salt_key, salt_index):
    try:
        extracted_index = int(encoded_payload[salt_index])
    except ValueError:
        return "Invalid salt index"
    
    if extracted_index != salt_index:
        return "Invalid salt index"
    
    encoded_payload_without_index = encoded_payload[:salt_index] + encoded_payload[salt_index+1:]
    
    try:
        decoded_payload_with_salt = base64.b64decode(encoded_payload_without_index).decode()
    except (base64.binascii.Error, ValueError):
        return "Invalid encoding"
    
    if decoded_payload_with_salt.endswith(salt_key):
        decoded_payload = decoded_payload_with_salt[:-len(salt_key)]
        return decoded_payload
    else:
        return "Invalid salt key"
