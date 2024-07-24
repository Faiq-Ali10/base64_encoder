import pytest
from base64_encoder.encoder import encode_payload

def test_encode_payload():
    payload = "Hello, World!"
    salt_key = "s3cr3t"
    salt_index = 5
    encoded = encode_payload(payload, salt_key, salt_index)
    assert isinstance(encoded, str)
    assert len(encoded) > len(payload)
