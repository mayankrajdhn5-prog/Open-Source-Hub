"""
Polyalphabetic Vigenere cipher encryption and decryption.
"""
def vigenere_encrypt(text: str, key: str) -> str:
    res = []
    key = key.lower()
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('a')
            res.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else: res.append(ch)
    return "".join(res)
