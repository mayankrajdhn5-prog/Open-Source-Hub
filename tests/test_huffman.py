"""
Unit test suite for Huffman tree encoding.
"""
from compression.huffman_coding import build_huffman_codes

def test_huffman():
    codes = build_huffman_codes("abracadabra")
    assert "a" in codes
    assert len(codes["a"]) < len(codes["c"])
