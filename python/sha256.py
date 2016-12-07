import hashlib
for i in range(100):
    m = hashlib.sha256()
    m.update(str(i))
    print i, "".join("{:02x}".format(ord(c)) for c in m.digest())
