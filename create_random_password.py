"""It creates random pasword."""

import string
import secrets

alphabet = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
alphabet += string.digits  # 0123456789

print(
    """Do you use punctuation?(y/n) Punctuation are !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
)
ans = input()
if ans.lower() == "y":
    alphabet += string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print("Set length of the password.")
password_length = int(input())

password = "".join(secrets.choice(alphabet) for i in range(password_length))

print(password)
