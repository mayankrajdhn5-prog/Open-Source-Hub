"""
Classic Caesar substitution cipher with configurable rotation shift.
"""
def caesar_encrypt(text: str, shift: int = 3) -> str:
    res = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            res.append(chr((ord(ch) - base + shift) % 26 + base))
        else: res.append(ch)
    return "".join(res)

def caesar_decrypt(text: str, shift: int = 3) -> str:
    return caesar_encrypt(text, -shift)
