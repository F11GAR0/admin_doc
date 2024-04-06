import hashlib

def validate_password(password, hash):

    return hashlib.md5(password.encode()).hexdigest() is hash