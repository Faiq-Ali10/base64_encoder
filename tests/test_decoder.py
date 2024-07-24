import pytest
from base64_encoder.decoder import decode_payload

def test_decode_payload():
    payload = "Hello, World!"
    salt_key = "s3cr3t"
    salt_index = 5
    encoded = "SGVsbG8sIFdv5cr3tcmxkIQ=="
    decoded = decode_payload(encoded, salt_key, salt_index)
    assert decoded == payload

    # Test with incorrect salt index
    incorrect_index = 4
    decoded_incorrect_index = decode_payload(encoded, salt_key, incorrect_index)
    assert decoded_incorrect_index == "Invalid salt index"

    # Test with incorrect salt key
    incorrect_salt_key = "wrong_key"
    decoded_incorrect_key = decode_payload(encoded, incorrect_salt_key, salt_index)
    assert decoded_incorrect_key == "Invalid salt key"
