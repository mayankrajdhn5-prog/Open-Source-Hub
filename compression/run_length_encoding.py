"""
Lossless Run-Length Encoding (RLE) string data compression.
"""
def rle_encode(text: str) -> str:
    if not text: return ""
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]: count += 1
        else:
            encoded.append(f"{count}{text[i - 1]}")
            count = 1
    encoded.append(f"{count}{text[-1]}")
    return "".join(encoded)

def rle_decode(data: str) -> str:
    import re
    tokens = re.findall(r'(\d+)(.)', data)
    return "".join(char * int(count) for count, char in tokens)
