import hashlib

def calculate_sha256_hash(item):
    return hashlib.sha256(str(item).encode('utf-8')).hexdigest()
