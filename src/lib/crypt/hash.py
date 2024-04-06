import hashlib

def hash_password(password) -> str:

    return hashlib.md5(password.encode()).hexdigest()

def validate_password(password, hash) -> bool:

    return hash_password(password) == hash
