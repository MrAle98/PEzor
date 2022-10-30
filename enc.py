from io import StringIO
import gzip, base64, subprocess, os, hashlib, shutil, re, donut, importlib, sys


shellcodePath=sys.argv[1]
outshellcodePath=sys.argv[2]

with open(shellcodePath, 'rb') as f:
	shellcode = bytearray(f.read())
	f.close()
key = bytearray(os.urandom(16))
k=0
for i in range(len(shellcode)):
	if k == len(key):
		k = 0
	print("before "+str(shellcode[i]))
	shellcode[i] = shellcode[i] ^ key[k]
	print("after "+str(shellcode[i]))
	k = k + 1

with open(f"{outshellcodePath}.bin","wb") as f:
	f.write(bytes(shellcode))
	f.close()
with open(f"{outshellcodePath}.key","wb") as f:
	f.write(bytes(key))
	f.close()
b64shellcode=base64.b64encode(bytes(shellcode))
b64key=base64.b64encode(bytes(key))
with open("enc_shellcode_b64","wb") as f:
	f.write(b64shellcode)
print(b64key.decode())
