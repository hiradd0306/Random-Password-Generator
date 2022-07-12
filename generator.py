import secrets
import string


# Chracters that can be used in a password
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    puncs = string.punctuation

    avail_chars = letters + digits + puncs

    password = ''.join(secrets.choice(avail_chars) for i in range(length))
    return password
