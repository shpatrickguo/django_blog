from django.db.models import TextField
from cryptography.fernet import Fernet

from billing.utils import make_encryption_key

ENCRYPTION_KEY = make_encryption_key('hello-world-256')

def encrypt(value):
    if value is None or value == '':
        return value
    encoded = value.encode()
    return Fernet(ENCRYPTION_KEY).encrypt(encoded)

def decrypt(value):
    if value is None or value == '':
        return value
    decrypted = Fernet(ENCRYPTION_KEY).decrypt(value)
    return str(decrypted, encoding='utf8')

class EncryptedTextField(TextField):
    def from_db_value(self, value, expression, connection):
        return decrypt(value)

    def to_python(self, value):
        return decrypt(value)

    def get_prep_value(self, value):
        return encrypt(value)
