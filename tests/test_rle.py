"""
Unit test suite for Run-Length Encoding.
"""
from compression.run_length_encoding import rle_encode, rle_decode

def test_rle():
    data = "WWWWWWAAAAAABBBB"
    enc = rle_encode(data)
    assert rle_decode(enc) == data
