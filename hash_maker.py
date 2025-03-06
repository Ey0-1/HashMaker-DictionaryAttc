import hashlib


hash = hashlib.sha1("A!".encode("utf-8")).hexdigest() # A! = Password
print(str(hash))