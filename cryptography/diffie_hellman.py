"""
Diffie-Hellman cryptographic key exchange protocol implementation.
"""
def generate_shared_secret(private_key: int, peer_public_key: int, prime: int) -> int:
    return pow(peer_public_key, private_key, prime)

def compute_public_key(private_key: int, generator: int, prime: int) -> int:
    return pow(generator, private_key, prime)
