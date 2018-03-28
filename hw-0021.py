import os
import base64
from hashlib import sha256
from hmac import HMAC


def hash_password(password, salt=None):

    if salt is None:
        salt = os.urandom(8)

    assert 8 == len(salt)
    assert isinstance(salt, bytes)

    if isinstance(password, str):
        password = password.encode('utf-8')

    assert isinstance(password, bytes)

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()
    return salt + result


def validate_password(hashed, input_password):
    return hashed == hash_password(input_password, salt=hashed[:8])


hashed = hash_password('dfds123.ds')
assert validate_password(hashed, 'dfds123.ds')

print(hashed)
print(base64.b64encode(hashed))
