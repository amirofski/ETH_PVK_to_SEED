import mnemonic
import hashlib

def private_key_to_seed() -> str:
    # Ask for the private key
    private_key = input("Please enter the private key: ")

    # Convert the private key to bytes
    private_key_bytes = bytes.fromhex(private_key)

    # Hash the private key bytes with SHA-256
    hash_bytes = hashlib.sha256(private_key_bytes).digest()

    # Convert the hash bytes to a mnemonic seed phrase
    seed_phrase = mnemonic.Mnemonic('english').to_mnemonic(hash_bytes)

    # Print the seed phrase
    print(seed_phrase)

    return seed_phrase

private_key_to_seed()
