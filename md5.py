import hashlib
i = input("Enter a password: ")
o = bytes(i, 'utf-8')
hash_obj = hashlib.md5(o)
print(hash_obj.hexdigest())
